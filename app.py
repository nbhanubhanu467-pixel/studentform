
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            usn TEXT,
            email TEXT,
            phone TEXT,
            course TEXT,
            gender TEXT
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    usn = request.form["usn"]
    email = request.form["email"]
    phone = request.form["phone"]
    course = request.form["course"]
    gender = request.form["gender"]

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, usn, email, phone, course, gender)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, usn, email, phone, course, gender))

    conn.commit()
    conn.close()

    return """
    <h2>Student Registered Successfully!</h2>
    <a href="/">Register Another Student</a>
    """


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
