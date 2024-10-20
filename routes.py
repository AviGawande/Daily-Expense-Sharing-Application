from flask import request, jsonify,Response
from app import app,mongo
from models import User, Expense
from bson import json_util, ObjectId
import json
import re
import csv
from io import StringIO

# Email validation regex pattern
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    # Validate email
    if 'email' not in data or not EMAIL_REGEX.match(data['email']):
        return jsonify({"error": "Invalid email address"}), 400

    # Validate name
    if 'name' not in data or not data['name'].strip():
        return jsonify({"error": "Name is required"}), 400

    # Validate mobile number (assuming it should be a string of 10 digits)
    if 'mobile' not in data or not re.match(r'^\d{10}$', data['mobile']):
        return jsonify({"error": "Invalid mobile number. It should be 10 digits."}), 400

    if User.find_by_email(data['email']):
        return jsonify({"error": "Email already exists"}), 400
    
    result = User.create(email=data['email'], name=data['name'], mobile=data['mobile'])
    return jsonify({"message": "User created successfully", "user_id": str(result.inserted_id)}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if not ObjectId.is_valid(user_id):
        return jsonify({"error": "Invalid user ID"}), 400
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return json.loads(json_util.dumps(user))

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json

    # Validate required fields
    required_fields = ['amount', 'description', 'split_method', 'payer_id', 'splits']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validate amount
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return jsonify({"error": "Invalid amount. Must be a positive number."}), 400

    # Validate payer
    if not ObjectId.is_valid(data['payer_id']):
        return jsonify({"error": "Invalid payer ID"}), 400
    payer = User.find_by_id(data['payer_id'])
    if not payer:
        return jsonify({"error": "Payer not found"}), 404

    # Validate split method
    if data['split_method'] not in ['equal', 'exact', 'percentage']:
        return jsonify({"error": "Invalid split method. Must be 'equal', 'exact', or 'percentage'."}), 400

    splits = data['splits']
    total_percentage = sum(split.get('percentage', 0) for split in splits)
    total_exact = sum(split.get('amount', 0) for split in splits)

    if data['split_method'] == 'equal':
        equal_amount = data['amount'] / len(splits)
        for split in splits:
            split['amount'] = equal_amount
    elif data['split_method'] == 'exact' and total_exact != data['amount']:
        return jsonify({"error": "The sum of exact amounts must equal the total expense amount"}), 400
    elif data['split_method'] == 'percentage' and total_percentage != 100:
        return jsonify({"error": "The sum of percentages must equal 100%"}), 400

    result = Expense.create(
        amount=data['amount'],
        description=data['description'],
        split_method=data['split_method'],
        payer_id=data['payer_id'],
        splits=splits
    )
    return jsonify({"message": "Expense added successfully", "expense_id": str(result.inserted_id)}), 201



@app.route('/expenses/user/<user_id>', methods=['GET'])
def get_user_expenses(user_id):
    if not ObjectId.is_valid(user_id):
        return jsonify({"error": "Invalid user ID"}), 400
    
    pipeline = [
        {
            '$match': {
                '$or': [
                    {'payer_id': user_id},
                    {'splits.user_id': user_id}
                ]
            }
        },
        {
            '$project': {
                'description': 1,
                'amount': 1,
                'split_method': 1,
                'payer_id': 1,
                'user_amount': {
                    '$cond': {
                        'if': {'$eq': ['$payer_id', user_id]},
                        'then': '$amount',
                        'else': {
                            '$arrayElemAt': [
                                {'$filter': {
                                    'input': '$splits',
                                    'as': 'split',
                                    'cond': {'$eq': ['$$split.user_id', user_id]}
                                }},
                                0
                            ]
                        }
                    }
                }
            }
        }
    ]
    
    expenses = list(mongo.db.expenses.aggregate(pipeline))
    return json.loads(json_util.dumps(expenses))


@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    expenses = Expense.find_all()
    return json.loads(json_util.dumps(list(expenses)))

@app.route('/balance-sheet/download', methods=['GET'])
def download_balance_sheet():
    # Get all users and expenses
    users = list(User.find_all())
    expenses = list(Expense.find_all())

    # Initialize balance sheet
    balance_sheet = {str(user['_id']): {'name': user['name'], 'balance': 0} for user in users}

    # Calculate balances
    for expense in expenses:
        payer_id = str(expense['payer_id'])
        balance_sheet[payer_id]['balance'] += expense['amount']
        
        for split in expense['splits']:
            user_id = str(split['user_id'])
            if 'amount' in split:
                balance_sheet[user_id]['balance'] -= split['amount']
            elif 'percentage' in split:
                balance_sheet[user_id]['balance'] -= expense['amount'] * split['percentage'] / 100

    # Prepare CSV data
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerow(['User ID', 'Name', 'Balance'])
    for user_id, data in balance_sheet.items():
        csv_writer.writerow([user_id, data['name'], f"{data['balance']:.2f}"])

    # Create response
    response = Response(csv_data.getvalue(), mimetype='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    return response