# 🚀 TeamFlow AI

TeamFlow AI is a modern AI-powered team collaboration and productivity platform built with FastAPI and PostgreSQL. The goal of the project is to help teams manage projects, tasks, meetings, and workflows while leveraging AI for smarter decision-making.

---

## ✨ Features

### ✅ Authentication Module

* User Registration
* User Login
* JWT Authentication
* OAuth2 Password Flow
* Protected API Endpoints

### 🚧 Upcoming Features

* Team Management
* Project Management
* Task Management
* AI Task Prioritization
* AI Meeting Summaries
* Notifications
* Analytics Dashboard

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* JWT Authentication
* Passlib (bcrypt)

### Tools

* Git
* GitHub
* pgAdmin
* VS Code
* Uvicorn

---

## 📂 Project Structure

```text
TeamFlow AI/
│
├── backend/
├── frontend/
├── docs/
├── README.md
├── CHANGELOG.md
└── .gitignore
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone <repository-url>
```

### Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 📚 Development Status

Current Sprint:

**Sprint 1.5 – Infrastructure**

Completed:

* Authentication Module
* PostgreSQL Integration
* Alembic Migration Setup
* OAuth2 Authentication
* Protected Routes

---

## 📄 License

This project is developed for learning, portfolio building, and future production deployment.
