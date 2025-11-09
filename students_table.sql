-- ========================================================
-- Assignment 3 - Question 1
-- PostgreSQL Database Setup Script
-- Creates the 'students' table and inserts sample data
-- ========================================================

-- CREATE DATABASE studentdb;

-- Switch to the database
-- \c studentdb;

-- Create the table
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

-- Insert initial data
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

-- Verify table content 
-- SELECT * FROM students;
