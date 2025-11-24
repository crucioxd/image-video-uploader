# FastAPI Media Upload & Authentication Project

A complete backend API built with **FastAPI**, featuring:

- 🔐 **User authentication** (JWT-based) using **FastAPI-Users**
- 📤 **Image & Video uploading** using **ImageKit.io**
- 🗄️ **SQLite database** using SQLAlchemy + Async session
- 🧵 **User ↔ Posts one‑to‑many relationship**
- 📦 Project managed with **uv** + pyproject.toml
- 🚀 Production-ready structure

This README provides:

- 📚 Full explanation of project structure
- 🛠️ Installation & setup guide
- 🔌 API documentation
- 🖼️ How to add screenshots/images
- 📁 Folder structure

---

## 📁 Project Structure

```
project/
│── app/
│   ├── app.py              # Main FastAPI routes
│   ├── db.py               # Database & models (User, Post)
│   ├── images.py           # ImageKit config
│   ├── schemas.py          # Pydantic models
│   ├── users.py            # FastAPI-Users auth config
│
│── main.py                 # Runs the FastAPI app
│── pyproject.toml          # Dependencies managed by uv
│── .gitignore              # Excludes env, DB, etc
│── .env                    # Sensitive API keys
│── README.md               # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone <your-repo-url>
cd project
```

### 2️⃣ Create & Activate Virtual Environment (uv)

```
uv venv
uv sync
```

### 3️⃣ Add Required Environment Variables

Create a `.env` file:

```
IMAGEKIT_PUBLIC_KEY=your_key
IMAGEKIT_PRIVATE_KEY=your_key
IMAGEKIT_URL_ENDPOINT=your_endpoint
DATABASE_URL=sqlite+aiosqlite:///./test.db
SECRET_KEY=your_secret
```

> ⚠️ **NEVER commit your `.env` file**. It is ignored in `.gitignore`.

### 4️⃣ Run the Server

```
uv run fastapi dev main.py
```

Server will start at:
👉 [http://localhost:8000](http://localhost:8000)

---

## 🔐 Authentication (FastAPI Users)

This project includes full JWT authentication:

- User registration → `/auth/register`
- User login (JWT) → `/auth/jwt/login`
- Reset password → `/auth/forgot-password`
- Verify email → `/auth/verify`
- Get user info → `/users/me`

Schemas used:

- `UserRead`
- `UserCreate`
- `UserUpdate`

Authentication backend uses:

```python
JWTStrategy(secret=SECRET, lifetime_seconds=3600)
```

---

## 🧵 Database Models

### 👤 User Model

- Inherits from `SQLAlchemyBaseUserTableUUID`
- Has **one-to-many** relation with Post

### 📝 Post Model

Each post includes:

- id (UUID)
- user_id (ForeignKey → user.id)
- caption
- url (ImageKit URL)
- file_type (image/video)
- file_name
- created_at

Relationship:

```python
User.posts → list of posts
Post.user → owner user
```

---

## 🚀 Upload API

### Endpoint

```
POST /upload
```

### Uploads:

- Images
- Videos

Flow:

1. Temporary local file created
2. File uploaded to ImageKit
3. Database entry created

Example request (Postman / Thunder Client):

- `file`: form-data → upload file
- `caption`: text

Response:

```json
{
  "id": "uuid",
  "caption": "hello world",
  "url": "https://ik.imagekit.io/...",
  "file_type": "image",
  "file_name": "example.jpg",
  "created_at": "2025-02-10T10:20:00"
}
```

---

## 📥 Feed API

### Endpoint

```
GET /feed
```

Returns posts sorted by latest first.

---

## 📦 Dependencies

Main libraries used:

- FastAPI
- FastAPI-Users
- SQLAlchemy Async
- ImageKit.io SDK
- Uvicorn
- aiosqlite

All dependencies are in `pyproject.toml`.

---

## 📌 Git Best Practices

- Never commit `.env`
- Commit DB files only if needed (your `test.db` should be ignored)
- Use meaningful commit messages

Example commit:

```
feat(auth): implement JWT auth with FastAPI-Users
```

---

## ✨ Future Improvements

- Add pagination for feed
- Add profile pictures
- Add like/comments models
- Add rate limiting

---

## ❤️ Puneet

Made with love while learning FastAPI.

If you need improvements, diagrams, or more docs, let me know!
