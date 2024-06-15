import sqlite3

class Like:
    def __init__(self, db, post_id, user_id):
        self.db = db
        self.post_id = post_id
        self.user_id = user_id

    def add_like(self):
        try:
            self.db.execute('INSERT INTO likes (post_id, user_id) VALUES (?, ?)', (self.post_id, self.user_id))
            self.db.commit()
            print("Like added successfully!")
        except sqlite3.Error as e:
            print(f"Error adding like: {e}")

