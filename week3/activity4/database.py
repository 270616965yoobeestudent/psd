import sqlite3

DATABASE_NAME = "activity4.db"


def create_tables():
    with sqlite3.connect(DATABASE_NAME) as connection:
      cursor = connection.cursor()
      cursor.execute(
        """
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );

        CREATE TABLE author_book (
            author_id INTEGER,
            book_id INTEGER,
            PRIMARY KEY (author_id, book_id),
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        );
    """
    )
