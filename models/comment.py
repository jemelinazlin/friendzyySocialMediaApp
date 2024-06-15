# models/comment.py

import sqlite3

class Comment:
    def __init__(self, db, post_id, user_id, content):
        self.db = db
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    def add_comment(self):
        try:
            self.db.execute('INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)', (self.post_id, self.user_id, self.content))
            self.db.commit()
            print("Comment added successfully!")
        except sqlite3.Error as e:
            print(f"Error adding comment: {e}")
