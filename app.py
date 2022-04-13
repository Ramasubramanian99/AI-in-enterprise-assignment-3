from flask import Flask, jsonify, request
import student_controller
from db import create_tables

app = Flask(__name__)

# Get all the student details
@app.route('/students', methods=["GET"])
def get_students():
    students = student_controller.get_students()
    return jsonify(students)

# Insert the details of one student
@app.route("/student", methods=["POST"])
def insert_student():
    student_details = request.get_json()
    id = student_details["id"]
    first_name = student_details["first_name"]    
    last_name = student_details["last_name"]
    amount_due = student_details["amount_due"]
    dob = student_details["dob"]
    result = student_controller.insert_student(first_name, last_name, amount_due, id, dob)
    return jsonify(result)

# Update the details of a particular student
@app.route("/student/<id>", methods=["PUT"])
def update_student(id):
    student_details = request.get_json()
    first_name = student_details["first_name"]    
    last_name = student_details["last_name"]
    amount_due = student_details["amount_due"]
    dob = student_details["dob"]
    result = student_controller.update_student(first_name, last_name, amount_due, dob, id)
    return jsonify(result)

# Delete the student details of one particular student
@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
    result = student_controller.delete_student(id)
    return jsonify(result)

# Get the details of one particular student
@app.route("/student/<id>", methods=["GET"])
def get_student_by_id(id):
    student = student_controller.get_by_id(id)
    return jsonify(student)

if __name__ == "__main__":
    create_tables()
    
    app.run(host='127.0.0.1', port=5000, debug=False)