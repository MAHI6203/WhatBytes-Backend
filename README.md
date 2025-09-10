# Healthcare Backend API

This project is a backend system for a healthcare application built with Django and Django REST Framework. It provides a RESTful API for managing users, patients, and doctors.

---

## Features

* **JWT Authentication:** Secure user registration and login using JSON Web Tokens.
* **Patient Management:** Full CRUD (Create, Read, Update, Delete) operations for patient records, accessible only by the authenticated user who created them.
* **Doctor Management:** Full CRUD operations for doctor records.
* **Patient-Doctor Mapping:** API endpoints to assign doctors to patients and manage those relationships.

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** djangorestframework-simplejwt

---

## Setup and Installation

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

* Python 3.10+
* PostgreSQL

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MAHI6203/WhatBytes-Backend.git](https://github.com/MAHI6203/WhatBytes-Backend.git)
    cd WhatBytes-Backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the environment variables:**
    Create a `.env` file in the project root and add your database credentials and a secret key.
    ```ini
    SECRET_KEY='your-secret-key'
    DEBUG=True
    DB_NAME='healthcare_db'
    DB_USER='your_db_user'
    DB_PASSWORD='your_db_password'
    DB_HOST='localhost'
    DB_PORT='5432'
    ```

5.  **Run the database migrations:**
    ```bash
    python3 manage.py migrate
    ```

6.  **Start the development server:**
    ```bash
    python3 manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

Here is a list of the available API endpoints.

| Method | Endpoint                    | Description                           | Authentication |
| :----- | :-------------------------- | :------------------------------------ | :------------- |
| `POST` | `/api/auth/register/`       | Register a new user                   | Not Required   |
| `POST` | `/api/auth/login/`          | Log in to get a JWT token             | Not Required   |
| `POST` | `/api/patients/`            | Add a new patient                     | Required       |
| `GET`  | `/api/patients/`            | Get all patients for the current user | Required       |
| `GET`  | `/api/patients/<id>/`       | Get details of a specific patient     | Required       |
| `POST` | `/api/doctors/`             | Add a new doctor                      | Required       |
| `GET`  | `/api/doctors/`             | Get all doctors                       | Not Required   |
| `POST` | `/api/mappings/`            | Assign a doctor to a patient          | Required       |
| `GET`  | `/api/mappings/<patient_id>/` | Get doctors for a specific patient    | Required       |