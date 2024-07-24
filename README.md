# Contacts API

This project creates a REST API for storing and managing contacts using FastAPI and SQLAlchemy.

## Functionality

The API allows you to perform the following actions:
- Create a new contact
- Getting a list of all contacts
- Getting one contact by its identifier
- Update an existing contact
- Delete a contact
- Search for contacts by first name, last name, or email address
- Get a list of contacts with birthdays for the next 7 days

## Technologies used.

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)

## Requirements

- Python 3.12
- Virtual environment for Python (recommended)

## Installing and running

1. Cloning the repository

    bash
    git clone https://github.com/your-username/contacts_api.git
    cd contacts_api
    ```

2. Creating and activating a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate # for Windows use `venv\Scripts\activate`
    ```

3. Installing dependencies

    ```bash
    pip install fastapi uvicorn sqlalchemy pydantic
    ```

4. Project structure

    ```plaintext
    contacts_api/
    └── app/
        ├── __init__.py
        ├── main.py
        ├── models.py
        ├── schemas.py
        ├── crud.py
        └── database.py
    ```

5. Starting the project

    ```bash
    uvicorn app.main:app --reload
    ```



6. API documentation

    After the project is launched, the documentation will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Examples of use

### Add and delete a new contact

```bash
curl -X POST "http://127.0.0.1:8000/contacts/" -H "Content-Type: application/json" -d '{
  "first_name": "John"
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "birthday": "1990-01-01",
  "additional_info": "Some additional info"
}’```


curl -X DELETE "http://127.0.0.1:8000/contacts/{contact_id}"
