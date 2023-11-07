# user_database.py
import sqlite3
import bcrypt
import logging

class UserDatabase:
    def __init__(self):
        try:
            self.connection = sqlite3.connect('user_db.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as sq:
            print("Error: {sq}")
            logging.error(sq)

    def add_user(self, username, password):
        try:
            password = self.hash_password(password)
            self.cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)', (username, password))
            self.connection.commit()
        except sqlite3.Error as sq:
            print("Error: {sq}")
            logging.error(sq)

    def get_password(self, username):
        try:
            self.cursor.execute('SELECT password FROM users WHERE username=?', (username,))
            return self.cursor.fetchone()
        except sqlite3.Error as sq:
            print("Error: {sq}")
            logging.error(sq)
    
    def hash_password(self, password):
        try:
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        except sqlite3.Error as sq:
            print("Error: {sq}")
            logging.error(sq)

    def check_password(self, password, hashed):
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed)
        except sqlite3.Error as sq:
            print("Error: {sq}")
            logging.error(sq)

    def close(self):
        try:
            self.connection.close()
        except sqlite3.Error as sq:
            print("Error: {sq}")
            logging.error(sq)
