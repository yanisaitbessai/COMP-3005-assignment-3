# Assignment 3 – Question 1  
### Database Interaction with PostgreSQL and Python  

**Course:** COMP 3005 
**Instructor:** Abdelghny Orogat 
**Student Name:** Yanis Ait Bessai
**Student ID:** 101313744 
**Date:** 11/08/2025

---

## Video demonstration
- https://youtu.be/vSs1Nh6ivnA 

## Overview
This project demonstrates how to connect a Python application to a **PostgreSQL** database and perform the four fundamental **CRUD operations** (Create, Read, Update, Delete).  
The program interacts with a database named `studentdb` containing a single table called `students`.  
All operations are executed using the **psycopg2** library for PostgreSQL in Python.

---

## Database Schema

**Table:** `students`

| Column | Data Type | Constraints |
|:--------|:-----------|:-------------|
| student_id | SERIAL | Primary Key |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| enrollment_date | DATE |  |

---

### **Install Requirements**

- Make sure **PostgreSQL** and **Python 3.10+** are installed on your computer.  
- Ensure the PostgreSQL server is running.
- Open a terminal and install the required Python library:
  ```bash
  python -m pip install psycopg2

**Create the Database**

- Open pgAdmin or psql.
- Create a new database:
"CREATE DATABASE studentdb;"

Inside the new database, run the contents of students_table.sql:

"CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"

you can see the table by then typing:
"SELECT * FROM students;"

**Configure the Connection**

Open app.py and update your PostgreSQL credentials:

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="studentdb",
        user="postgres",
        password=" your_postgres_password"
    )


Replace " your_postgres_password" with your actual PostgreSQL password.

**Run the Program**

Open a terminal in your project folder and run:
python -m pip install psycopg2
or
py -m pip install psycopg2

And now enter,
- python app.py
or
- py app.py

**Verify the Output**

You should see output similar to:

=== PostgreSQL Student Database ===

All Students:
1 | John | Doe | john.doe@example.com | 2023-09-01
2 | Jane | Smith | jane.smith@example.com | 2023-09-01
3 | Jim | Beam | jim.beam@example.com | 2023-09-02

Added student: Alice Johnson
Updated email for student ID 1
Deleted student ID 2

**Check the Database in pgAdmin**

After running the program:
- Open pgAdmin → Database: studentdb
- Right-click on the students table → View/Edit Data → All Rows
Confirm:
- One new student was added.
- One student’s email was updated.
- One student was deleted.


