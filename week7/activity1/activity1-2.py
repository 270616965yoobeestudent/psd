import sqlite3
import time

class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect("database.db")  # New connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result


class OrderService:
    def get_orders(self, user_id):
        conn = sqlite3.connect("database.db")  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result


if __name__ == "__main__":
    start = time.time()
    UserService().get_user(1)
    OrderService().get_orders(1)
    print(time.time() - start)

    # FROM 100027 records.
    # execute time is 0.07268404960632324
