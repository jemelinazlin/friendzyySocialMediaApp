import sqlite3

DATABASE_NAME = './social_media.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            content TEXT,
                            image_url TEXT,  
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            new_column TEXT,  -- Add your new column here
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            post_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            content TEXT NOT NULL,
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (post_id) REFERENCES posts (id),
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS likes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            post_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            FOREIGN KEY (post_id) REFERENCES posts (id),
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )''')

        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def close_connection(conn):
    conn.close()
