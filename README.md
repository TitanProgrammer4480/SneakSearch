# Sneak Search

This is a Flask-based web application that allows users to perform searches using Google, DuckDuckGo, and Brave (currently disabled). The app includes user authentication with login, signup, and session management.

## 🚀 Features
- User authentication (Signup, Login, Logout)
- Search functionality using Google and DuckDuckGo
- Dashboard for logged-in users
- SQLite database for user management

## 📌 Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

## 🛠 Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TitanProgrammer4480/SneakSearch
   cd flask-search-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```python
   from app import db
   db.create_all()
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the app in your browser at:
   ```
   http://127.0.0.1:5000/
   ```

## 📜 License
This project is licensed under the MIT License.
