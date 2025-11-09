"""
Assignment 3 - Question 1
Database Interaction with PostgreSQL
Author: Yanis Ait Bessai
Date: 2025/11/05

This program connects to a PostgreSQL database and performs CRUD operations
on the 'students' table.
"""

import psycopg2
from psycopg2 import sql

# ---------- Database Connection ----------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="studentdb",
        user="postgres",      
        password="student"  
    )

# ---------- CRUD Functions ----------

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


def deleteStudent(student_id):
    """Delete a student by ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    print(f"\nDeleted student ID: {student_id}")
    cur.close()
    conn.close()


# ---------- Demonstration ----------
if __name__ == "__main__":
    getAllStudents()

    addStudent("Alice", "Johnson", "alice.johnson@example.com", "2023-09-10")
    getAllStudents()

    updateStudentEmail(1, "john.newemail@example.com")
    getAllStudents()

    deleteStudent(2)
    getAllStudents()
