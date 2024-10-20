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
   - `cd GrowthX-Backend`
   - Install the Requirements file for project:
      - `pip install -r requirements. txt `
- 4.Run this command on the terminal(ensure to activate the virtualenv and install the dependencies):
   - `uvicorn main:app --reload`
   - visit this url `http://127.0.0.1:8000/` on browser.
- 5.And your backend system is running locally.


  # Results:
  I have attached the snapshots of the each enpoint working successfully along with Postman Urls each.

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
     - a.For Equal Split: 
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
  
   - b.For Exact Split
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

  

   
 
   - 4.Upload an Assignment (as a user):
     - Method: POST
     - URL: `http://localhost:8000/upload`
     - Auth:
         - Use "Basic Auth" (enter `testuser` and `testpassword`).
     - Body: Select "Raw" and then "JSON" from the dropdown in the Body tab:
       ```
       {
          "task": "Complete Python assignment",
           "admin_username": "testadmin"
        }
       ```
     - ![Screenshot 2024-10-09 215032](https://github.com/user-attachments/assets/603c9518-dc84-4cf1-8282-e055baaf5d59)
  
   - 5.Get All Admins:
     - Method: GET
     - URL: `http://localhost:8000/admins`
     - **No Authentication**: This is a public endpoint. You can simply send the request without any authentication.
     - ![Screenshot 2024-10-09 215142](https://github.com/user-attachments/assets/83cec580-f5ad-49e5-bc0e-fc3e3f2155d2)

   - 6.View Assignments (as an admin):
     - Method: GET
     - URL: `http://localhost:8000/assignments`
     - Auth:
         - Use "Basic Auth" (enter `testadmin` and `adminpassword`).
     - ![Screenshot 2024-10-09 215327](https://github.com/user-attachments/assets/d14316b0-e7da-4372-8d03-c9d1b90b5371)
    
   - 7.Accept an Assignment:
     - Method: POST
     - URL: `http://localhost:8000/assignments/{assignment_id}/accept`
     - Auth:
         - Use "Basic Auth" (enter `admin2` and `Admin@222`).
     - Replace {assignment_id}: with the actual assignment ID you want to accept.
     - ![Screenshot 2024-10-10 134419](https://github.com/user-attachments/assets/573d52e9-b973-40d5-b328-aebed74b7e5c)

   - 8.Reject an Assignment:
     - Method: POST
     - URL: `http://localhost:8000/assignments/{assignment_id}/reject`
     - Auth:
         - Use "Basic Auth" (enter `admin2` and `Admin@222`).
     - Replace {assignment_id}: with the actual assignment ID you want to reject..
     - ![Screenshot 2024-10-10 135336](https://github.com/user-attachments/assets/7fcc6b98-15d6-4c44-8891-8ba60dc119b1)

## I am also posting the Postman Collection here where i tested all the API Enpoints:
https://www.postman.com/abhigawande123/workspace/remote-bricks-apis/collection/36164059-d97f0850-f40b-4490-abae-0d8594ec5d97?action=share&creator=36164059

