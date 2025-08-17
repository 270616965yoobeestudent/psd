from .base_manager import BaseManager
from database import DATABASE_NAME
import sqlite3


class LecturerManager(BaseManager):
    def get(self, id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM lecturers WHERE id = ?", (id,))
            return cursor.fetchone()

    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM lecturers")
            return cursor.fetchall()

    def add(self, name):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO lecturers (name) VALUES (?)", (name,))
            return cursor.lastrowid

    def delete(self, id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM lecturers WHERE id = ?", (id,))

    def update(self, id, name):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE lecturers SET name = ? WHERE id = ?",
                (
                    name,
                    id,
                ),
            )
