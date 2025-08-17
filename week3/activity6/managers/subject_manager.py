from .base_manager import BaseManager
from database import DATABASE_NAME
import sqlite3


class SubjectManager(BaseManager):
    def get(self, id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM subjects WHERE id = ?
                LEFT JOIN courses ON subjects.course_id = courses.id
                """,
                (id,),
            )
            return cursor.fetchone()

    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM subjects 
                LEFT JOIN courses ON subjects.course_id = courses.id
                """
            )
            return cursor.fetchall()

    def list_of_course(self, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM subjects 
                WHERE course_id = ?
                """,
                (course_id,),
            )
            return cursor.fetchall()

    def add(self, name, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO subjects (name, course_id) VALUES (?, ?)",
                (
                    name,
                    course_id,
                ),
            )
        return cursor.lastrowid

    def delete(self, id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM subjects WHERE id = ?", (id,))

    def update(self, id, name, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE subjects SET name = ?, course_id = ? WHERE id = ?",
                (
                    name,
                    course_id,
                    id,
                ),
            )
