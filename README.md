# Task Management Application
IT-2305
Ubaidullauly Azamat
Sayat Temirlan
Shaimerden Atembek

A Flask-based web application for managing tasks with user authentication and Kanban-style organization.

##GitHub repo
https://github.com/ShadowFighterr/Backend-Final/blob/main/app.py

## Live Demo
https://task-management-it2305.onrender.com/

## Features
- User registration/login
- CRUD operations for tasks
- Kanban board interface
- Drag-and-drop task status updates
- User profile management
- Secure password handling
- PostgreSQL database
- Responsive design

## Technologies
- Python 3.11
- Flask 3.0.2
- Flask-SQLAlchemy 3.1.1
- Flask-Login 0.6.3
- PostgreSQL
- Bootstrap 5
- Gunicorn
- Render (Deployment)

## Installation

### Prerequisites
- Python 3.11+
- PostgreSQL
- pip

### Local Setup
1. Clone repo:
```bash
git clone https://github.com/ShadowFighterr/Backend-Final.git
cd Backend-Final
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac)
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create `.env` file:
```ini
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost/dbname
FLASK_APP=app.py
FLASK_ENV=development
```

5. Initialize database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run application:
```bash
flask run
```

## Deployment on Render
1. Create new Web Service
2. Connect GitHub repository
3. Set environment variables:
   - `SECRET_KEY`: Random string
   - `DATABASE_URL`: From Render PostgreSQL dashboard
   - `FLASK_APP`: app.py
4. Build Command:
```bash
pip install -r requirements.txt && flask db upgrade
```
5. Start Command:
```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

## API Endpoints
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| / | GET | Home page | No |
| /register | GET/POST | User registration | No |
| /login | GET/POST | User login | No |
| /logout | GET | User logout | Yes |
| /add | POST | Create new task | Yes |
| /delete/<id> | GET | Delete task | Yes |
| /edit/<id> | GET/POST | Edit task | Yes |
| /profile | GET/POST | User profile | Yes |
| /update_status/<id> | POST | Update task status (AJAX) | Yes |

## Project Structure
```
.
├── app.py
├── config.py
├── forms.py
├── models.py
├── requirements.txt
├── migrations/
├── static/
│   └── css/
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    └── profile.html
```

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create PR
