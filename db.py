import sqlite3
DATABASE_NAME = "students.db"


def get_db():
    #connect to the database instance and return it
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

# This function will get called everytime the app is initialized
def create_tables():
    # The SQL query below creates a table called students in the students.db file
    # with the columns id, first_name, last_name, amount_due, dob
    tables = [
        """CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
				amount_due REAL NOT NULL,
				dob TEXT NOT NULL
            )
            """
    ]
    # get the instance of the database and store it in db
    db = get_db()
    # get the current state of the database
    cursor = db.cursor()
    # loop through the tables and executes the SQL command in our case we have only one
    # table therefore only one command
    for table in tables:
        cursor.execute(table)