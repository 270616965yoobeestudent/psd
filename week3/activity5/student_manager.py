from database import create_connection
import sqlite3


def add_student(name, address):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Oops! Something went wrong.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")

def seed_students():
    students = view_students()
    if not students:
        add_student("John Doe", "123 Main St")
        add_student("Jane Smith", "456 Elm St")
