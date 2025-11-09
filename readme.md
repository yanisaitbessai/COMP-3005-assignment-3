\# Assignment 3 – Question 1  

\### Database Interaction with PostgreSQL and Python  



\*\*Course:\*\* COMP 3005 

\*\*Instructor:\*\* Abdelghny Orogat 

\*\*Student Name:\*\* Yanis Ait Bessai

\*\*Student ID:\*\* 101313744 

\*\*Date:\*\* 11/08/2025



---



\## Overview

This project demonstrates how to connect a Python application to a \*\*PostgreSQL\*\* database and perform the four fundamental \*\*CRUD operations\*\* (Create, Read, Update, Delete).  

The program interacts with a database named `studentdb` containing a single table called `students`.  

All operations are executed using the \*\*psycopg2\*\* library for PostgreSQL in Python.



---



\## Database Schema



\*\*Table:\*\* `students`



| Column | Data Type | Constraints |

|:--------|:-----------|:-------------|

| student\_id | SERIAL | Primary Key |

| first\_name | TEXT | NOT NULL |

| last\_name | TEXT | NOT NULL |

| email | TEXT | NOT NULL, UNIQUE |

| enrollment\_date | DATE |  |



---



\### \*\*Install Requirements\*\*



\- Make sure \*\*PostgreSQL\*\* and \*\*Python 3.10+\*\* are installed on your computer.  

\- Ensure the PostgreSQL server is running.

\- Open a terminal and install the required Python library:

&nbsp; ```bash

&nbsp; python -m pip install psycopg2



\*\*Create the Database\*\*



\- Open pgAdmin or psql.

\- Create a new database:

"CREATE DATABASE studentdb;"



Inside the new database, run the contents of students\_table.sql:



"CREATE TABLE students (

&nbsp;   student\_id SERIAL PRIMARY KEY,

&nbsp;   first\_name TEXT NOT NULL,

&nbsp;   last\_name  TEXT NOT NULL,

&nbsp;   email      TEXT NOT NULL UNIQUE,

&nbsp;   enrollment\_date DATE

);



INSERT INTO students (first\_name, last\_name, email, enrollment\_date) VALUES

('John', 'Doe', 'john.doe@example.com', '2023-09-01'),

('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),

('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"



\*\*Configure the Connection\*\*



Open app.py and update your PostgreSQL credentials:



def get\_connection():

&nbsp;   return psycopg2.connect(

&nbsp;       host="localhost",

&nbsp;       database="studentdb",

&nbsp;       user="postgres",

&nbsp;       password=" your\_postgres\_password"

&nbsp;   )





Replace " your\_postgres\_password" with your actual PostgreSQL password.



\*\*Run the Program\*\*



Open a terminal in your project folder and run:

\- python app.py

or

\- py app.py



\*\*Verify the Output\*\*



You should see output similar to:



=== PostgreSQL Student Database ===



All Students:

1 | John | Doe | john.doe@example.com | 2023-09-01

2 | Jane | Smith | jane.smith@example.com | 2023-09-01

3 | Jim | Beam | jim.beam@example.com | 2023-09-02



Added student: Alice Johnson

Updated email for student ID 1

Deleted student ID 2



\*\*Check the Database in pgAdmin\*\*



After running the program:

\- Open pgAdmin → Database: studentdb

\- Right-click on the students table → View/Edit Data → All Rows

Confirm:

\- One new student was added.

\- One student’s email was updated.

\- One student was deleted.

