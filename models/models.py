import sqlite3

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


class Post:
    def __init__(self, db, user_id, content):
        self.db = db
        self.user_id = user_id
        self.content = content

    def create_post(self):
        self.db.execute('INSERT INTO posts (user_id, content) VALUES (?, ?)', (self.user_id, self.content))
        self.db.commit()
        print("Post created successfully!")


class Comment:
    def __init__(self, db, post_id, user_id, content):
        self.db = db
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    def add_comment(self):
        self.db.execute('INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)', (self.post_id, self.user_id, self.content))
        self.db.commit()
        print("Comment added successfully!")


class Like:
    def __init__(self, db, post_id, user_id):
        self.db = db
        self.post_id = post_id
        self.user_id = user_id

    def add_like(self):
        self.db.execute('INSERT INTO likes (post_id, user_id) VALUES (?, ?)', (self.post_id, self.user_id))
        self.db.commit()
        print("Like added successfully!")
