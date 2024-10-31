## Name: Li Zhou

### Rest api for Question 1

# Student API

This is a simple RESTful API built with Python and Flask that supports basic CRUD operations (Create, Read, Update, Delete) for a Student entity. Each student has an ID, Name, Grade, and Email.

## Features

- **GET /students**: Retrieve a list of all students.
- **GET /students/{id}**: Retrieve details of a student by ID.
- **POST /students**: Add a new student.
- **PUT /students/{id}**: Update an existing student by ID.
- **DELETE /students/{id}**: Delete a student by ID.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your machine.
- **pip**: Python package manager, which usually comes with Python.

### 1. Installation

Setting Up
Navigate to your directory:
```bash
mkdir rest-api-8916-mid
cd rest-api-8916-mid
```
Initialize Git and push to GitHub:
```bash
Copy code
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/zhou0265/rest-api-8916-mid.git
git push -u origin main

```

### 2. Create a virtual environment:

```bash
Copy code
python3 -m venv venv

```
### 3. Activate the virtual environment:

```bash
source venv/bin/activate
```
### 4. Install dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run locally
```bash
python app.py
```

### Set up on Azure

