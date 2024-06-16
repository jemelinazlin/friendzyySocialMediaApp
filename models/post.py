import sqlite3
class Post:
    def __init__(self, conn, user_id, content):
        self.conn = conn
        self.user_id = user_id
        self.content = content

    def create_post(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, content) VALUES (?, ?)
            ''', (self.user_id, self.content))
            self.conn.commit()
            print("Post created successfully.")

        except sqlite3.Error as e:
            print(f"Error creating post: {e}")
