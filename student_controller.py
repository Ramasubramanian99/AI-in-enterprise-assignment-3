from db import get_db


def insert_student(first_name, last_name, amount_due, id, dob):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO students(first_name, last_name, amount_due, id, dob) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [first_name, last_name, amount_due, id, dob])
    db.commit()
    return True


def update_student(first_name, last_name, amount_due, id, dob):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE students SET first_name = ?, last_name = ?, amount_due = ?, dob = ? WHERE id = ?"
    cursor.execute(statement, [first_name, last_name, amount_due, dob])
    db.commit()
    return True


def delete_student(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, first_name, last_name, amount_due, dob FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_students():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, first_name, last_name, amount_due, dob FROM students"
    cursor.execute(query)
    return cursor.fetchall()