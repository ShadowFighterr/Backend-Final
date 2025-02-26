# Task Management Application

IT-2305  
Ubaidullauly Azamat 231244  
Atembek Shaimerden 230299  
Sayat Temirlan 231383  

## Introduction
This is a simple Task Management application built with Flask, SQLAlchemy, PostgreSQL, and Flask-WTF for form handling. The application allows users to register, log in, create, update, delete, and view their tasks. Authentication and authorization are implemented using Flask-Login, and CSRF protection is enabled for security.

## Installation
1. Clone the repository:
   
   git clone https://github.com/ShadowFighterr/Backend-Final
   cd Backend-Final
   

2. Create and activate a virtual environment:
   
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Set up the database and environment variables:
   - Create a .env file in the root directory with the following content:
     
     SECRET_KEY=your_secret_key
     DATABASE_URL=postgresql+psycopg2://postgres:@localhost/tasks
     

5. Initialize the database:
   
   flask db init
   flask db migrate
   flask db upgrade
   

6. Start the application:
   
   flask run
   

7. Open the browser and go to:
   
   http://127.0.0.1:5000/
   

## Usage
- Register: /register
- Login: /login
- View Tasks: /
- Add Task: /add
- Edit Task: /edit/<id>
- Delete Task: /delete/<id>
- Update Task Status: /update_status/<id>

## Authentication and Authorization
Most routes require authentication using Flask-Login. After logging in, users can manage their own tasks securely.

### ✅ How to log in:
1. Go to /login and enter your email and password.
2. If successful, you will be redirected to your task list.

### ✅ How to test API endpoints:
For testing authentication and protected routes, you can use Postman:
1. Log in and retrieve the session cookies.
2. Include the cookies in the request headers when accessing protected routes.

## Test User Credentials (Optional)
To make testing easier, you can create a user like this:

- Email: test@example.com
- Password: password123

Or register your own user at /register.

## Features
- User registration and login
- Flask-Login authentication
- Task creation, editing, and deletion
- CSRF protection
- PostgreSQL database with SQLAlchemy ORM
- Flask-WTF form validation

## Dependencies
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- WTForms
- psycopg2

## Deployment
The application is deployed on Render and is accessible at:

🔗 https://task-management-it2305.onrender.com/
