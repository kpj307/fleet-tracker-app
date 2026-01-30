# 🚗 Fleet Tracker

Fleet Tracker is a **full‑stack vehicle finance management application** built with **Django REST Framework** and **React**. It helps individuals or companies track vehicle income, expenses, and profits with powerful time‑based filters and a clean, responsive UI.

---

## ✨ Features

### 🔐 Authentication

* JWT‑based login & registration
* Secure, user‑scoped data (each user sees only their vehicles)

### 🚘 Vehicle Management

* Add, edit, delete vehicles
* View per‑vehicle financial summaries

### 💰 Income & Expense Tracking

* Add, edit, delete income entries
* Add, edit, delete expense entries
* Expense categories via dropdown

### ⏱ Period Filters (System‑Wide)

* Weekly (calendar week)
* Monthly (calendar month)
* Annually (calendar year)
* Custom date range

  * No data shown unless **both dates** are selected

### 📱 Responsive UI

* Mobile‑friendly navbar with hamburger menu
* Clean modals for edit forms

---

## 🧱 Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* SimpleJWT
* SQLite 

### Frontend

* React (Vite)
* React Router
* Axios
* CSS Modules

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/fleet-tracker.git
cd fleet-tracker
```

---

## 🐍 Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## ⚛️ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🔑 Environment Variables

### Frontend (`api.js`)

```js
const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});
```

---

## 📡 API Endpoints (Sample)

```text
POST   /api/token/          → Login
POST   /api/register/       → Register
GET    /api/vehicles/       → List vehicles
POST   /api/vehicles/       → Add vehicle
PATCH  /api/vehicles/:id/   → Edit vehicle
DELETE /api/vehicles/:id/   → Delete vehicle

GET    /api/income/
POST   /api/income/
PATCH  /api/income/:id/
DELETE /api/income/:id/

GET    /api/expenses/
POST   /api/expenses/
PATCH  /api/expenses/:id/
DELETE /api/expenses/:id/
```

---

## 🧠 Design Decisions

* Backend enforces calendar‑accurate date ranges
* Custom filters return **no data** unless fully specified
* Minimal, maintainable CSS (no UI libraries)

---

## 🧑‍💻 Author

**Fleet Tracker** was built as a production‑ready finance tracking system.

Feel free to fork, extend, and improve it 🚀

---

## 📄 License

MIT License
