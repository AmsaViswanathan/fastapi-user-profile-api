# Python Backend Engineer Take Home Assessment

This project is a backend REST API built using FastAPI and PostgreSQL.

It provides CRUD operations for managing users with proper validation, error handling, and clean project structure.

This project is developed as part of a Python Backend Engineer take home assessment.

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest

---

## Features

- Create User API
- Get User API
- Update User API
- Delete User API
- PostgreSQL Database Integration
- External API Integration
- Request & Response Validation
- Error Handling

---

## API Endpoints

POST /users  
Create a new user  

GET /users/{id}  
Get user details  

PUT /users/{id}  
Update user details  

DELETE /users/{id}  
Delete a user  

---

## Database Schema

Table Name: users  

Columns:
- id (Primary Key)
- name
- email (Unique)

---

## External API

Random User API is used to demonstrate third-party API integration.

---

## Validation

All requests and responses are validated using Pydantic models.

---

## Error Handling

- 201 - Resource Created  
- 404 - Resource Not Found  
- 422 - Validation Error  

---

## Project Structure

backend-assessment  
app  
tests  
.env  
requirements.txt  
README.md  

---

## Conclusion

This project satisfies all the requirements of the Python Backend Engineer assessment.

It follows clean backend architecture with proper database integration, validation, testing, and API design.
