class Post:
    def __init__(self, conn, user_id, content, image_url=None):
        self.conn = conn
        self.user_id = user_id
        self.content = content
        self.image_url = image_url  # Optional image_url parameter

    def create_post(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, content, image_url) VALUES (?, ?, ?)
            ''', (self.user_id, self.content, self.image_url))
            self.conn.commit()
            print("Post created successfully.")

        except sqlite3.Error as e:
            print(f"Error creating post: {e}")
