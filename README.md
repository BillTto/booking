# 🤖 Django REST API Bot Constructor

## 📌 Project Description

Backend API for creating and managing chatbot scenarios.

The system allows:
- Creating bots
- Creating conversation scenarios
- Adding steps to scenarios
- Running scenarios via API

---

## 🛠 Tech Stack

- Python 3.11
- Django
- Django REST Framework
- SQLite
- Git / GitHub

---

## 🚀 Features

✅ CRUD API for Bots  
✅ CRUD API for Scenarios  
✅ CRUD API for Steps  
✅ Scenario run endpoint  
✅ Django Admin panel  

---

## 🔗 API Endpoints

### Bots
- `GET /bots/`
- `POST /bots/`

### Scenarios
- `GET /scenarios/`
- `POST /scenarios/`

### Run Scenario
- `POST /scenarios/{id}/run/`

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/BillTto/booking.git
cd booking
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
