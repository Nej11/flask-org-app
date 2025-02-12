# 🏢 Flask Organization Management App  

A Flask-based web application for managing users and teams within an organization. This app allows users to add, edit, and delete users, assign them to teams, and manage teams efficiently.  

## 🚀 Features  
✅ Add, edit, and delete users  
✅ Create and manage teams  
✅ View user and team details  
✅ Simple and clean UI with Bootstrap  
✅ Secure database handling with Flask SQLAlchemy  

## 🛠 Technologies Used  
- **Backend:** Flask (Python), Flask SQLAlchemy, Flask Migrate  
- **Database:** MySQL  
- **Frontend:** HTML, Bootstrap  
- **Version Control:** Git & GitHub  

## 📦 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/Nej11/flask-org-app.git
cd flask-org-app
```
2️⃣ Set Up Virtual Environment
```sh
python -m venv venv  
source venv/bin/activate  # Mac/Linux  
venv\Scripts\activate  # Windows  
```
3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
4️⃣ Configure the Database
Ensure MySQL is running
Update config.py with your MySQL credentials
Run database migrations:
```sh
flask db upgrade
```
5️⃣ Run the Application
```sh
python app.py
```
