# Full-Stack Project: Frontend, Django Chat, and AWS Lambda Functions

## Introduction
This project is a full-stack application that integrates responsive frontend development, a Django-based chat application, and AWS Lambda functions for cloud-based tasks. The application provides a dynamic, user-friendly interface with real-time chat functionality, and it leverages AWS services to perform specific cloud operations like adding numbers and storing files.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (Responsive Web Design)
- **Backend**: Django, WebSockets
- **Cloud**: AWS Lambda, S3
- **Database**: SQLite (for Django chat app)

---

## 1. Frontend Development

### Features:
- Fixed Navbar
- Responsive Layout: Left Menu, Main Content, Right Panel
- Footer
- Collapsible Left Menu
- Dynamic Resizing Based on Screen Width

### Instructions:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
2. Open the index.html file in your browser to see the webpage in action.

3. The JavaScript function automatically adjusts the page's width based on the screen size, making it responsive across devices.

---

## 2.  Django Chat Application

### Features:
- User Sign Up/Login
-Collapsible User List
-Chat with Other Users
-WebSocket Integration for Real-Time Messaging
-Message History Storage in Database

### Instructions:
#### Running the Django Chat Application:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository


2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

3. Activate the virtual environment:
- On Windows:
   ```bash
   .\venv\Scripts\activate
- On macOS/Linux:
   ```bash
   source venv/bin/activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

5. Set up the database:
   ```bash
   python manage.py migrate

6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser

7. Run the Django development server:
   ```bash
   python manage.py runserver

8. Navigate to http://127.0.0.1:8000 in your browser, sign up or log in, and start chatting with other users.

   
   ---

## 3.  AWS Lambda Functions

### Features:
- AWS Lambda Function to Add Two Numbers
- AWS Lambda Function to Store Files in S3 Bucket

### Instructions:
#### Running AWS Lambda Functions:

1. Sign in to your AWS account.

2. Create an S3 bucket if you don't already have one.

3. Create the Lambda functions:
 - Add Numbers Function: Deploy a simple Lambda function to add two numbers. You can find the Lambda code in the /lambda/add_numbers.py file.
 - Store File in S3 Function: Deploy another Lambda function to upload files to your S3 bucket. The code is in the /lambda/store_file.py file.

4. Test the Lambda functions through the AWS console or using the AWS CLI.

5. For the Add Numbers Function, pass two numbers as input parameters to get the result.

6. For the Store File in S3 Function, upload a document or PDF file to your S3 bucket by invoking the Lambda function.

---

### How to Run All Tasks:

#### Here is a consolidated guide to running all three tasks:
1. Frontend:
- Navigate to the folder containing the frontend files and open the index.html file in a browser to view the responsive webpage.

2. Django Chat Application:
- Follow the instructions under the Django Chat Application section to set up and run the Django server. Ensure you have the necessary dependencies and database migrations set up.

3. AWS Lambda Functions:
- Log in to your AWS account, set up the Lambda functions, and test them as described in the AWS Lambda Functions section.
