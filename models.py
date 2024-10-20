from app import mongo
from bson import ObjectId

class User:
    @staticmethod
    def create(email,name,mobile):
        return mongo.db.users.insert_one({"email":email,"name":name,"mobile":mobile})
    
    @staticmethod
    def find_by_id(user_id):
        return mongo.db.users.find_one({"_id":ObjectId(user_id)})
    
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email":email})
    
    @staticmethod
    def find_all():
        return mongo.db.users.find()
    

class Expense:
    @staticmethod
    def create(amount,description,split_method,payer_id,splits):
        return mongo.db.expenses.insert_one({
            "amount":amount,
            "description":description,
            "split_method":split_method,
            "payer_id":payer_id,
            "splits":splits
        })
    
    @staticmethod
    def find_by_id(expense_id):
        return mongo.db.expenses.find_one({"_id":ObjectId(expense_id)})
    
    @staticmethod
    def find_by_user(user_id):
        return mongo.db.expenses.find({"payer_id":user_id})
    
    @staticmethod
    def find_all():
        return mongo.db.expenses.find()