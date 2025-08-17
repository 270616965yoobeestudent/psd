import sqlite3

DATABASE_NAME = "activity4.db"


def create_tables():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.executescript(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS lecturers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                course_id INTEGER,
                FOREIGN KEY(course_id) REFERENCES courses(id)
            );
            CREATE TABLE IF NOT EXISTS student_course (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY(student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            );
            CREATE TABLE IF NOT EXISTS student_subject (
                student_id INTEGER,
                subject_id INTEGER,
                PRIMARY KEY(student_id, subject_id),
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(subject_id) REFERENCES subjects(id)
            );
            CREATE TABLE IF NOT EXISTS lecturer_subject (
                lecturer_id INTEGER,
                subject_id INTEGER,
                PRIMARY KEY(lecturer_id, subject_id),
                FOREIGN KEY(lecturer_id) REFERENCES lecturers(id),
                FOREIGN KEY(subject_id) REFERENCES subjects(id)
            );
            """
        )


def seed_data():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        student_count = cursor.fetchone()[0]
        if student_count > 0:
            return

        cursor.executescript(
            """
            INSERT OR IGNORE INTO students (id, name) VALUES
                (1, 'Alice'),
                (2, 'Bob'),
                (3, 'Charlie');
            INSERT OR IGNORE INTO courses (id, name) VALUES
                (1, 'Computer Science'),
                (2, 'Mathematics');
            INSERT OR IGNORE INTO lecturers (id, name) VALUES
                (1, 'Dr. Smith'),
                (2, 'Prof. Johnson');
            INSERT OR IGNORE INTO subjects (id, name, course_id) VALUES
                (1, 'Data Structures', 1),
                (2, 'Algorithms', 1),
                (3, 'Calculus', 2),
                (4, 'Linear Algebra', 2);
            INSERT OR IGNORE INTO student_course (student_id, course_id) VALUES
                (1, 1),  -- Alice in Computer Science
                (2, 2),  -- Bob in Mathematics
                (3, 1);  -- Charlie in Computer Science
            INSERT OR IGNORE INTO student_subject (student_id, subject_id) VALUES
                (1, 1),  -- Alice in Data Structures
                (1, 2),  -- Alice in Algorithms
                (2, 3),  -- Bob in Calculus
                (2, 4),  -- Bob in Linear Algebra
                (3, 2);  -- Charlie in Algorithms
            INSERT OR IGNORE INTO lecturer_subject (lecturer_id, subject_id) VALUES
                (1, 1),  -- Dr. Smith teaches Data Structures
                (1, 2),  -- Dr. Smith teaches Algorithms
                (2, 3),  -- Prof. Johnson teaches Calculus
                (2, 4);  -- Prof. Johnson teaches Linear Algebra
            """
        )
