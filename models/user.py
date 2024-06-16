import sqlite3
class User:
    def __init__(self, db, username, password):
        self.db = db
        self.username = username
        self.password = password

    def sign_up(self):
        try:
            self.db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
            self.db.commit()
            print(f"User {self.username} created successfully!")
        except sqlite3.IntegrityError:
            print(f"User {self.username} already exists!")

    def log_in(self):
        cursor = self.db.execute('SELECT id FROM users WHERE username=? AND password=?', (self.username, self.password))
        result = cursor.fetchone()

        if result:
            print(f"Welcome, {self.username}!")
            return result[0]
        else:
            print("Invalid username or password!")
            return None
