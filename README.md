# Python Backend Engineer Take Home Assessment

## Overview

This project is a REST API service built using FastAPI and PostgreSQL.  
It demonstrates backend engineering skills such as database integration, external API consumption, validation, testing, and clean architecture.

The service acts as a bridge between a local PostgreSQL database and a public external API.

---

## Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic Validation
- Pytest Testing

---

## Project Structure

backend-assessment/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes.py
│   └── external_api.py
│
├── tests/
│   └── test_api.py
│
├── .env
├── requirements.txt
└── README.md

---

## Database Schema

Table: users

| Field | Type |
|------|------|
| id | Integer (Primary Key) |
| name | String |
| email | String (Unique) |

---

## External API Integration

This project integrates with a public API:

https://randomuser.me/api

The POST `/users` endpoint fetches user data from this external API before storing it in the PostgreSQL database.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users | Create user using external API |
| GET | /users/{id} | Get user by ID |
| PUT | /users/{id} | Update user name |
| DELETE | /users/{id} | Delete user |

---

## Validation

- Request and response validation using Pydantic
- Email validation using EmailStr
- Required field enforcement

---

## Error Handling

- 201 Created
- 404 Not Found
- 422 Validation Error
- Proper HTTPException handling

---

## Testing

Testing is implemented using Pytest and FastAPI TestClient.
