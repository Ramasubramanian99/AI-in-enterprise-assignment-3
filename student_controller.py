from db import get_db

# Function to update the student details in the database
def insert_student(first_name, last_name, amount_due, id, dob):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO students(first_name, last_name, amount_due, id, dob) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [first_name, last_name, amount_due, id, dob])
    db.commit()
    return True

# Function to update the details of the student from the database
def update_student(first_name, last_name, amount_due, dob, id): 
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE students SET first_name = ?, last_name = ?, amount_due = ?, dob = ? WHERE id = ?"
    cursor.execute(statement, [first_name, last_name, amount_due, dob])
    db.commit()
    return True

# Function to delete the details of a particular student from the database
def delete_student(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

# Function to get the details of a single person based on ID from the database
def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, first_name, last_name, amount_due, dob FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

# Function to get the details of all the students
def get_students():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, first_name, last_name, amount_due, dob FROM students"
    cursor.execute(query)
    return cursor.fetchall()