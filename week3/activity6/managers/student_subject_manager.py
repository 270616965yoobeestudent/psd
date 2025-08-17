from .base_manager import BaseManager
from database import DATABASE_NAME
import sqlite3


class StudentSubjectManager(BaseManager):
    def get(self, student_id, subject_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_subject 
                WHERE student_id = ? AND subject_id = ? 
                LEFT JOIN students ON student_subject.student_id = students.id 
                LEFT JOIN subjects ON student_subject.subject_id = subjects.id
                """,
                (
                    student_id,
                    subject_id,
                ),
            )
            return cursor.fetchone()

    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_subject
                LEFT JOIN students ON student_subject.student_id = students.id  
                LEFT JOIN subjects ON student_subject.subject_id = subjects.id
                """
            )
            return cursor.fetchall()

    def list_of_student(self, student_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_subject
                LEFT JOIN students ON student_subject.student_id = students.id  
                LEFT JOIN subjects ON student_subject.subject_id = subjects.id
                LEFT JOIN courses ON course_id = courses.id
                WHERE student_id = ?
                """,
                (student_id,),
            )
            return cursor.fetchall()

    def list_of_course(self, student_id, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_subject
                LEFT JOIN students ON student_subject.student_id = students.id  
                LEFT JOIN subjects ON student_subject.subject_id = subjects.id
                WHERE student_id = ? AND course_id = ?
                """,
                (student_id, course_id),
            )
            return cursor.fetchall()

    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_subject
                LEFT JOIN students ON student_subject.student_id = students.id  
                LEFT JOIN subjects ON student_subject.subject_id = subjects.id
                """
            )
            return cursor.fetchall()

    def add(self, student_id, subject_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO student_subject (student_id, subject_id) VALUES (?, ?)",
                (
                    student_id,
                    subject_id,
                ),
            )

    def delete(self, student_id, subject_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM student_subject WHERE student_id = ? AND subject_id = ?",
                (
                    student_id,
                    subject_id,
                ),
            )

    def update(self):
        pass
