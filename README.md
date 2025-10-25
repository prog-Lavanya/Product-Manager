
# FastAPI Product Management System #
 Designed and implemented a backend API system using FastAPI for handling product data in a SQL Server database. Focused on environment management, middleware setup (CORS), and CRUD functionality for seamless data operations.


## About the Project
- Backend: FastAPI, SQLAlchemy, SQL Server — implemented by me
- Frontend: React UI (base template adapted from open-source)
- Integrated both for seamless product CRUD operations
  
---

## 🧩 Tech Stack

**Backend:**
- FastAPI
- SQLAlchemy
- Python-dotenv
- pyodbc
- MS SQL Server

**Frontend:**
- React.js
- Axios
- HTML / CSS / JavaScript

**Structure**
FAST_API_PROJECT/
│
├── main.py # FastAPI entry point
├── database.py # Database connection setup
├── database_models.py # SQLAlchemy ORM models
├── models.py # Pydantic models
├── .env # Environment variables (not pushed)
├── requirements.txt # Python dependencies
│
├── frontend/ # React frontend
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── package-lock.json
│
└── README.md

## 🧠 Setup Instructions
**Frontend Setup**
1. Entering into the frontend folder
   ```bash
   cd frontend
   
2. Installation of dependencies
   ```bash
   npm install 
3. Starting the frontend 
   ```bash
   npm start

**Backend Setup**
1. Create and activate a virtual environment:
   ```bash
   python -m venv myvenv
   myvenv\Scripts\activate  # (Windows)
   
2. Installation of dependencies
   ```bash
   pip install -r requirements.txt
3. Create your .env file
   ```env
   DATABASE_URL=nameOfDatabase+driver://<username>:<password>@<server>/<database>?driver=<driver_name>
4. Run fast api server
  ```bash
  uvicorn main: app --reload

