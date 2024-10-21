### This is the Backend Intern - Assignment for Backend Intern at Convin.ai

## Objective:
Daily Expense Sharing Application

### Technology Used:
- 1.Language and Framework:
   - Python
   - Flask

- 2.Database:
   - MongoDB .
   - MongoDB Compass

- 3.Testing:
   - Used Postman for Testing Client URLs.

### API Endpoints:
   - 1.User Endpoint.
      - Create User(POST).
      - Retrieve User Details(GET).
        
   - 2.Expense Endpoint.
      - Add Expense(POST)
      - Retrieve Individual User Expenses(GET).
      - Retrieve Overall Expenses(GET).
      - Download Balance Sheet(GET).
 
## How to SetUp this project locally and Test the Results:

- 1.Fork/Clone this repo:
   - `git clone https://github.com/AviGawande/Daily-Expense-Sharing-Application`
- 2.In the same directory create a virtual environment(venv):
   - Install dependencies if not. `pip install virtualenv`
   - Create a new Virtual.Env name myenv. `python -m venv myenv`
   - Activate the Virtual-Environment(myenv). `myenv\Scripts\activate`
- 3.CD into the project directory of clonned project:
   - `cd Daily-Expense-Sharing-Application`
   - Install the Requirements file for project:
      - `pip install -r requirements. txt `
- 4.Run this command on the terminal(ensure to activate the virtualenv and install the dependencies):
   - `flask run `
   - visit this url `http://127.0.0.1:5000/` on browser.
- 5.And your backend system is running locally.


  # Results:
  I have attached the snapshots of the each enpoint working successfully along with Collection of Postman URLs.

  - 1.Create User:
     - Method: POST
     - URL: `http://localhost:5000/users`
     - Body(raw JSON):
       ```
       {
       "email": "abhishek123@gmail.com",
       "name": "Abhishek Gawande",
       "mobile": "1111122222"
       }
       
       ```
     - ![Screenshot 2024-10-20 160411](https://github.com/user-attachments/assets/0b6fa4c4-2d3f-4cf4-ae36-b1fa9e40e296)

   
   - 2.Retrieve User Details:
     - Method: GET
     - URL: `http://localhost:5000/users/<user_id>`
      (Replace <user_id> with the ID returned when creating a user)--> Connect the backend-app with database(MongoDB) to get the IDs.
     - ![Screenshot 2024-10-20 195103](https://github.com/user-attachments/assets/d3ba81e1-7453-44af-add2-60cecd883448)

    
   - 3.Add Expense:
     - Method: POST
     - URL: `http://localhost:5000/expenses`
     - a. For Equal Split: 
       ```
       {
       "amount": 3000,
       "description": "Dinner",
       "payer_id": "<user_id>",
       "split_method": "equal",
       "splits": [
           {"user_id": "<user_id1>"},
           {"user_id": "<user_id2>"},
           {"user_id": "<user_id3>"}
       ]
       }
       ```
     -![Screenshot 2024-10-20 182133](https://github.com/user-attachments/assets/5cbe945b-4947-4135-bf9b-f88f81d8d61d)
  
     - b.For Exact Split:
       ```
       {
       "amount": 4299,
       "description": "Shopping",
       "payer_id": "<user_id>",
       "split_method": "exact",
       "splits": [
           {"user_id": "<user_id1>", "amount": 799},
           {"user_id": "<user_id2>", "amount": 2000},
           {"user_id": "<user_id3>", "amount": 1500}
       ]
       }
       ```
     - ![Screenshot 2024-10-20 182133](https://github.com/user-attachments/assets/cb740cd3-e606-405c-8dec-4515686a77f2)

     - c. For Percentage Split:
       ```
          {
       "amount": 1000,
       "description": "Party",
       "payer_id": "<user_id>",
       "split_method": "percentage",
       "splits": [
           {"user_id": "<user_id1>", "percentage": 50},
           {"user_id": "<user_id2>", "percentage": 25},
           {"user_id": "<user_id3>", "percentage": 25}
       ]
        }
       ```
     - ![Screenshot 2024-10-20 183250](https://github.com/user-attachments/assets/f8978ba3-a80e-424d-9ba6-c4460fd85c63)


  
   - 4.Retrieve Individual User Expenses :
     - Method: GET
     - URL: `http://localhost:5000/expenses/user/<user_id>`
     - (Replace <user_id> with an actual user ID)
     - ![Screenshot 2024-10-20 185756](https://github.com/user-attachments/assets/e3b45403-df69-451c-b85b-8bc81d62025d)

  
   - 5.Retrieve Overall Expenses :
     - Method: GET
     - URL: ` http://localhost:5000/expenses`
     - ![Screenshot 2024-10-20 192426](https://github.com/user-attachments/assets/bc650437-3790-4d6f-be90-61a0139ca941)


   - 6.Download the Balance Sheet:
     - Method: GET
     - URL: `http://localhost:5000/balance-sheet/download`
     - ![Screenshot 2024-10-20 194934](https://github.com/user-attachments/assets/64ec5c8f-a31b-4686-842f-056c3006727f)

    


## I am also posting the Postman Collection here where i tested all the API Enpoints:
https://www.postman.com/abhigawande123/workspace/convin/collection/36164059-b00fba34-3f3d-4d1e-b194-7f689ef1d507?action=share&creator=36164059

