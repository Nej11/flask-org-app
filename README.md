# Flask Organization Management App

A Flask-based web application for managing users and teams within an organization.

## 🚀 Features
- Add, edit, and delete users.
- Create and manage teams.
- View user and team details.
- Simple and clean UI with Bootstrap.

## 🛠 Technologies Used
- Flask (Python)
- Flask SQLAlchemy (Database ORM)
- Flask Migrate (Database migrations)
- MySQL (Database)
- Bootstrap (Frontend)

## 📦 Setup & Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Nej11/flask-org-app.git
cd flask-org-app

Set up a virtual environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

Install Dependencies
pip install -r requirements.txt

configure the database
(run migration)
flask db upgrade

run the app
python app.py
