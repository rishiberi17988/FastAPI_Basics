# FastAPI Basics

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)

A collection of projects built with **FastAPI**, covering REST API development, database integration, CRUD operations, and machine learning model deployment.

## Projects

### 1. Local API (`localAPI/`)
A patient management API using a JSON file for data storage.

- Create, view, update, and delete patient records.
- Retrieve individual patient details.
- Sort patients by height, weight, or BMI.
- Calculate BMI and classify results.

### 2. Database API (`dbAPI/`)
A database-backed patient management API built with FastAPI, SQLAlchemy, and MySQL.

- Perform CRUD operations on patient records.
- Use asynchronous database operations.
- Organize API routes using FastAPI routers.
- Manage patient data with SQLAlchemy models.

### 3. Machine Learning API (`mlAPI/`)
A machine learning prediction service that exposes a trained model through a REST API.

- Accept patient and lifestyle-related input features.
- Process inputs and derive additional features.
- Generate predictions using a trained machine learning model.
- Serve predictions through a FastAPI endpoint.

## Project Structure

```text
FastAPI_Basics/
├── dbAPI/
│   ├── main.py
│   ├── routers/
│   ├── models.py
│   ├── session.py
│   └── sql/
├── localAPI/
│   ├── main.py
│   └── patients.json
├── mlAPI/
│   ├── main.py
│   ├── model.pkl
│   ├── insurance.csv
│   ├── fastapi_ml_model.ipynb
│   └── streamlit.py
├── requirements.txt
├── test.py
└── LICENSE
```

## Learning Outcomes

- Building RESTful APIs using FastAPI.
- Validating request data and defining schemas with Pydantic.
- Implementing CRUD operations and handling API requests.
- Integrating MySQL databases using SQLAlchemy.
- Structuring applications with modular routers and models.
- Serving trained machine learning models through API endpoints.
- Understanding how backend APIs connect with data processing and machine learning workflows.
