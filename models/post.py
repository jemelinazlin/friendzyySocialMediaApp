import sqlite3
class Post:
    def __init__(self, conn, user_id, content, image_url=None):
        self.conn = conn
        self.user_id = user_id
        self.content = content
        self.image_url = image_url

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

    @staticmethod
    def view_feed(conn, user_id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE user_id = ?", (user_id,))
        posts = cursor.fetchall()
        for post in posts:
            print(f"Post ID: {post['id']}, Content: {post['content']}")

if __name__ == "__main__":
    conn = get_db_connection()

    post = Post(conn, user_id=1, content="This is a sample post.", image_url="https://example.com/image.jpg")
    post.create_post()

    close_connection(conn)