from .base_manager import BaseManager
from database import DATABASE_NAME
import sqlite3


class LecturerSubjectManager(BaseManager):
    def get(self, lecturer_id, subject_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM lecturer_subject 
                WHERE lecturer_id = ? AND subject_id = ? 
                LEFT JOIN lecturers ON lecturer_subject.lecturer_id = lecturers.id 
                LEFT JOIN subjects ON lecturer_subject.subject_id = subjects.id
                """,
                (
                    lecturer_id,
                    subject_id,
                ),
            )
            return cursor.fetchone()

    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM lecturer_subject
                LEFT JOIN lecturers ON lecturer_subject.lecturer_id = lecturers.id 
                LEFT JOIN subjects ON lecturer_subject.subject_id = subjects.id
                """
            )
            return cursor.fetchall()

    def list_of_lecturer(self, lecturer_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM lecturer_subject
                LEFT JOIN lecturers ON lecturer_subject.lecturer_id = lecturers.id 
                LEFT JOIN subjects ON lecturer_subject.subject_id = subjects.id
                LEFT JOIN courses ON course_id = courses.id
                WHERE lecturer_id = ?
                """,
                (lecturer_id,),
            )
            return cursor.fetchall()


    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM lecturer_subject
                LEFT JOIN subjects ON lecturer_subject.subject_id = subjects.id 
                LEFT JOIN subjects ON lecturer_subject.subject_id = subjects.id
                """
            )
            return cursor.fetchall()

    def add(self, lecturer_id, subject_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO lecturer_subject (lecturer_id, subject_id) VALUES (?, ?)",
                (
                    lecturer_id,
                    subject_id,
                ),
            )

    def delete(self, lecturer_id, subject_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM lecturer_subject WHERE lecturer_id = ? AND subject_id = ?",
                (
                    lecturer_id,
                    subject_id,
                ),
            )

    def update(self):
        pass
