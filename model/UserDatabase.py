# user_database.py
import sqlite3
import bcrypt

class UserDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('user_db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        ''')
        self.connection.commit()

    def add_user(self, username, password):
        password = self.hash_password(password)
        self.cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)', (username, password))
        self.connection.commit()

    def get_password(self, username):
        self.cursor.execute('SELECT password FROM users WHERE username=?', (username,))
        return self.cursor.fetchone()
    
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

    def close(self):
        self.connection.close()
