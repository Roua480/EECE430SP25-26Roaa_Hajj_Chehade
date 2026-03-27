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

## 🔹 Option 1: Run from Docker Hub

Pull and run the pre-built image:

```bash
docker pull roua780/player_list:latest
docker run -p 8000:8000 roua780/player_list:latest
