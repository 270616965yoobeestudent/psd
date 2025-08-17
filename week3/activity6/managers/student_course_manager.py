from .base_manager import BaseManager
from database import DATABASE_NAME
import sqlite3


class StudentCourseManager(BaseManager):
    def get(self, student_id, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_course 
                WHERE student_id = ? AND course_id = ? 
                LEFT JOIN students ON student_course.student_id = students.id 
                LEFT JOIN courses ON student_course.course_id = courses.id
                """,
                (
                    student_id,
                    course_id,
                ),
            )
            return cursor.fetchone()

    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_course
                LEFT JOIN students ON student_course.student_id = students.id 
                LEFT JOIN courses ON student_course.course_id = courses.id
                """
            )
            return cursor.fetchall()

    def list_of_student(self, student_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_course
                LEFT JOIN students ON student_course.student_id = students.id 
                LEFT JOIN courses ON student_course.course_id = courses.id
                WHERE student_id = ?
                """,
                (student_id,),
            )
            return cursor.fetchall()


    def list(self):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM student_course
                LEFT JOIN students ON student_course.student_id = students.id 
                LEFT JOIN courses ON student_course.course_id = courses.id
                """
            )
            return cursor.fetchall()

    def add(self, student_id, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO student_course (student_id, course_id) VALUES (?, ?)",
                (
                    student_id,
                    course_id,
                ),
            )

    def delete(self, student_id, course_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM student_course WHERE student_id = ? AND course_id = ?",
                (
                    student_id,
                    course_id,
                ),
            )

    def update(self):
        pass
