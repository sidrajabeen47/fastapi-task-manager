# FastAPI Task Manager

A lightweight, asynchronous REST API for managing tasks and to-do lists, built using **FastAPI**, **SQLAlchemy ORM**, and **SQLite**.

## 🚀 Features
* **FastAPI framework** with automatic Swagger UI (`/docs`) generation.
* **SQLAlchemy ORM** integration for clean database interactions.
* **SQLite Database** configuration handled seamlessly across multiple concurrent threads.
* Full validation using **Pydantic** data schemas.

---

## 🛠️ Project Structure

```text
projects/
│
├── env/               # Python virtual environment (ignored in git)
├── main.py            # API routes and server initialization
├── database.py        # SQLAlchemy engine and session configuration
├── models.py          # Database tables & Pydantic schemas
