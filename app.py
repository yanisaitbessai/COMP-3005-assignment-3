"""
Assignment 3 - Question 1
Database Interaction with PostgreSQL
Author: Yanis Ait Bessai
Date: 2025/11/05

This program connects to a PostgreSQL database and performs CRUD operations
(Create, Read, Update, Delete) on the 'students' table.
"""

import psycopg2
from psycopg2 import sql

# ==============================================================
# Function: get_connection()
# Purpose: Establish and return a connection to the PostgreSQL database
# Notes:
#   - The connection parameters (host, database, user, password)
#     must match your local PostgreSQL setup.
#   - The returned connection object is used by other functions
#     to execute SQL queries.
# ==============================================================
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="studentdb",
        user="postgres",      
        password="student"  
    )


# ==============================================================
# Function: getAllStudents()
# Purpose:
#   - Retrieve and display all student records from the 'students' table.
#   - Performs a simple SELECT query ordered by student_id.
# Steps:
#   1. Connect to the database.
#   2. Execute a SELECT * query.
#   3. Fetch all rows and print them to the console.
#   4. Close the cursor and connection.
# ==============================================================
def getAllStudents():
    """Retrieve and display all students."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY student_id;")
    rows = cur.fetchall()
    print("\nAll Students:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()


# ==============================================================
# Function: addStudent(first_name, last_name, email, enrollment_date)
# Purpose:
#   - Add a new student record into the 'students' table.
# Parameters:
#   first_name (str)  → Student's first name
#   last_name (str)   → Student's last name
#   email (str)       → Student's email address
#   enrollment_date (str) → Enrollment date in 'YYYY-MM-DD' format
# Steps:
#   1. Connect to the database.
#   2. Execute an INSERT query with parameterized values.
#   3. Commit the transaction.
#   4. Print confirmation message.
# ==============================================================
def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, email, enrollment_date))
    conn.commit()
    print(f"\nAdded student: {first_name} {last_name}")
    cur.close()
    conn.close()


# ==============================================================
# Function: updateStudentEmail(student_id, new_email)
# Purpose:
#   - Update the email address of an existing student.
# Parameters:
#   student_id (int)  → The unique ID of the student to update
#   new_email (str)   → The new email address to assign
# Steps:
#   1. Connect to the database.
#   2. Execute an UPDATE query targeting the student_id.
#   3. Commit the transaction.
#   4. Print a confirmation message showing the update.
# ==============================================================
def updateStudentEmail(student_id, new_email):
    """Update email for a given student."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students SET email = %s WHERE student_id = %s;
    """, (new_email, student_id))
    conn.commit()
    print(f"\nUpdated student {student_id}'s email to {new_email}")
    cur.close()
    conn.close()


# ==============================================================
# Function: deleteStudent(student_id)
# Purpose:
#   - Delete a student record based on their unique student_id.
# Parameters:
#   student_id (int)  → The ID of the student to be removed
# Steps:
#   1. Connect to the database.
#   2. Execute a DELETE query.
#   3. Commit the transaction.
#   4. Print a confirmation message.
# ==============================================================
def deleteStudent(student_id):
    """Delete a student by ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    print(f"\nDeleted student ID: {student_id}")
    cur.close()
    conn.close()


# ==============================================================
# Demonstration Section
# Purpose:
#   - This section runs automatically when the program is executed directly.
#   - It demonstrates all four CRUD operations in sequence:
#       1. Display all students (initial data)
#       2. Add a new student
#       3. Update a student's email
#       4. Delete a student record
#       5. Display all students again after each operation
# ==============================================================
if __name__ == "__main__":
    getAllStudents()

    addStudent("Alice", "Johnson", "alice.johnson@example.com", "2023-09-10")
    getAllStudents()

    updateStudentEmail(1, "john.newemail@example.com")
    getAllStudents()

    deleteStudent(2)
    getAllStudents()
