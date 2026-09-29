# FlyRank Internship - Backend Track | Week 2 Assignment A4
## Auth, Login & Protect (FastAPI + Supabase Auth)

A secure backend API built with **FastAPI** and **Supabase Auth** featuring user registration, secure login, JSON Web Token (JWT) verification, reusable middleware guards, and interactive Swagger UI documentation.

---

### 🚀 Features
- **Supabase Identity Provider Integration**: Secure password hashing and token generation handled via Supabase Auth.
- **Token Verification & Guard Middleware**: Custom FastAPI dependency (`Depends`) that extracts and validates bearer tokens on protected routes.
- **Interactive Swagger UI**: Fully documented endpoints with built-in Bearer Token authentication via `/docs`[cite: 1].

---

### 🛠️ API Reference

| Endpoint | Method | Purpose | Auth Required |
| :--- | :--- | :--- | :--- |
| `/auth/signup` | `POST` | Register a new user account[cite: 1] | None |
| `/auth/login` | `POST` | Authenticate credentials & return JWT[cite: 1] | None |
| `/auth/logout` | `POST` | End active user session[cite: 1] | Yes (`Bearer <token>`) |
| `/public/info` | `GET` | Read public open data[cite: 1] | None |
| `/protected/profile` | `GET` | Read private user profile data[cite: 1] | Yes (`Bearer <token>`) |
| `/protected/dashboard` | `GET` | Secure user dashboard[cite: 1] | Yes (`Bearer <token>`) |

---

### ⚙️ Getting Started & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Pixell20/Fly-Rank-Internship-P4](https://github.com/Pixell20/Fly-Rank-Internship-P4)
   Fly Rank Internship P4
   