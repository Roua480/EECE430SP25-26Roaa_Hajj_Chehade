# EECE430 - Software Engineering  
## Assignment 5 – Dockerized Django Project  

**Date:** March 2026  

---

# 🏐 Volleyball Player List Management

## 📌 Description
This project is a web application built using Django to manage a list of volleyball players.  
It supports full CRUD functionality (Create, Read, Update, Delete).

The application has been containerized using Docker to allow easy deployment and execution on any machine.

---

## ⚙️ Features
- Add a new volleyball player
- View all players
- Update player information
- Delete a player

---

## 🧾 Player Fields
- ID (auto-generated)
- Name
- Date Joined
- Position
- Salary / Payment
- Contact Person

---

## 🛠 Technologies Used
- Python  
- Django  
- SQLite  
- HTML (templates)  
- Docker  

---

## 📁 Project Structure
- `models.py` → database structure  
- `forms.py` → form handling  
- `views.py` → application logic (CRUD operations)  
- `urls.py` → routing (maps URLs to views)  
- `templates/` → frontend pages  
- `Dockerfile` → container configuration  

---

# 🐳 Running the Project (Docker)
(note: Docker must be installed and running)
## 🔹 Option 1: Run from Docker Hub

Pull and run the pre-built image:

```bash
docker pull roua780/player_list:latest
docker run -p 8000:8000 roua780/player_list:latest
```

Open in browser:  
👉 http://localhost:8000

---

## 🔹 Option 2: Build and Run Locally

```bash
docker build -t player_list .
docker run -p 8000:8000 player_list
```

Open in browser:  
👉 http://localhost:8000

---

# 💻 Running Without Docker 

Open terminal in the project folder

## 🔹 1. Create and activate virtual environment

```bash
py -3 -m venv venv
venv\Scripts\activate
```

## 🔹 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔹 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🔹 4. Run the server

```bash
python manage.py runserver
```

Open in browser:  
👉 http://127.0.0.1:8000/

---

## 📌 Notes
- Make sure Docker is installed and running before using Docker commands
- Port `8000` must be available on your machine
- Python 3 is required if running without Docker
