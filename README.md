# UpskillHub Backend

## 🚀 Project Overview
UpskillHub is an AI-powered learning roadmap platform that helps learners streamline their journey from beginner to expert in various tech stacks. The backend is built using **FastAPI** and provides structured learning paths based on user goals.

## 📌 MVP Features
### **1️⃣ User Management**
- `POST /users/register` → Register a user
- `POST /users/login` → Login with JWT authentication
- `GET /users/me` → Get user profile

### **2️⃣ Learning Roadmap**
- `POST /roadmaps/` → Create a personalized roadmap
- `GET /roadmaps/{user_id}` → Retrieve user's roadmap
- `PATCH /roadmaps/{id}` → Update roadmap progress

## 🛠 Tech Stack
- **FastAPI** - API framework
- **PostgreSQL** - Database
- **SQLAlchemy + Alembic** - ORM & Migrations
- **Pydantic** - Data validation
- **Redis** - Caching (optional)
- **Docker** - Containerization
- **JWT** - Authentication
- **uv** - Package management

## 🏗 Project Structure
```
/learning-roadmap-backend
│── /app
│   ├── /api             # API routes
│   ├── /models          # Database models
│   ├── /schemas         # Pydantic schemas
│   ├── /services        # Business logic
│   ├── /core            # Configs (DB, settings, middleware)
│   ├── main.py          # App entry point
│── .env                 # Environment variables
│── pyproject.toml       # Dependency management (uv)
│── Dockerfile           # Docker setup
│── README.md            # Documentation
│── alembic/             # Database migrations
│── tests/               # Unit tests
```

## 🔧 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/learning-roadmap-backend.git
cd learning-roadmap-backend
```

### **2️⃣ Install Dependencies using uv**
```sh
uv venv
uv pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables (.env file)**
Create a `.env` file and add:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/roadmap_db
SECRET_KEY=your_secret_key
REDIS_URL=redis://localhost:6379/0
```

### **4️⃣ Run Database Migrations**
```sh
alembic upgrade head
```

### **5️⃣ Start the Server**
```sh
uvicorn app.main:app --reload
```
API will be available at: `http://127.0.0.1:8000`

## 📬 API Testing
Use **Postman** or the built-in **Swagger UI**:
```
http://127.0.0.1:8000/docs
```

## 🐳 Docker Setup (Optional)
To run the project using Docker, use:
```sh
docker-compose up --build
```

## ✅ Next Steps
- Implement AI-powered personalized roadmap generation
- Add role-based access control
- Deploy to production

---
💡 **Contributors:** Your Name | developersekar1992@gmail.com

