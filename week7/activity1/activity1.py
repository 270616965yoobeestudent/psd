import sqlite3
import threading
import time


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = sqlite3.connect("database.db")
        return cls._instance

    def getConnection(self):
        return self._connection

    def closeConnection(self):
        self._connection.close()


class UserService:
    def __init__(self):
        self._db = DatabaseConnection()

    def get_user(self, user_id):
        conn = self._db.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()


class OrderService:
    def __init__(self):
        self._db = DatabaseConnection()

    def get_orders(self, user_id):
        conn = self._db.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        return cursor.fetchall()


if __name__ == "__main__":
    start = time.time()
    UserService().get_user(1)
    OrderService().get_orders(1)
    DatabaseConnection().closeConnection()
    print(time.time() - start)
    
    # FROM 100027 records.
    # execute time is 0.0722513198852539
