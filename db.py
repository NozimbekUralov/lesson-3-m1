import sqlite3


class Database:
    def __init__(self, db_name='users.db'):
        self.__conn = sqlite3.connect(db_name, check_same_thread=False)
        self.__cursor = self.__conn.cursor()

        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(150) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL
            )
        """)

        self.__conn.commit()

    def find_user(self, email: str):
        self.__cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
        return self.__cursor.fetchone()

    def add_user(self, email: str, password: str, first_name: str, last_name: str):
        self.__cursor.execute(
            f"INSERT INTO users (email, password, first_name, last_name) VALUES ('{email}', '{password}', '{first_name}', '{last_name}');",
        )
        self.__conn.commit()

DB = Database()
