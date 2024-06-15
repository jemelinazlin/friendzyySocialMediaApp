import sqlite3
from database.connection import get_db_connection, create_tables, close_connection
from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like

def main():
    conn = get_db_connection()

    create_tables(conn)

    while True:
        print("\nMenu:")
        print("1. Sign up")
        print("2. Log in")
        print("3. Create post")
        print("4. View feed")
        print("5. Add comment")
        print("6. Add like")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(conn, username, password)
            user.sign_up()

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(conn, username, password)
            user_id = user.log_in()
            if user_id:
                while True:
                    print("\nUser menu:")
                    print("1. Create post")
                    print("2. View feed")
                    print("3. Add comment")
                    print("4. Add like")
                    print("5. Log out")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        content = input("Enter post content: ")
                        post = Post(conn, user_id, content)
                        post.create_post()

                    elif user_choice == "2":
                        cursor = conn.execute('SELECT id, content, created_at FROM posts WHERE user_id=? ORDER BY created_at DESC', (user_id,))
                        posts = cursor.fetchall()

                        for post in posts:
                            print(f"\n{post['created_at']} - {post['content']}")
                            print("--------------------")
                            print("Comments:")
                            cursor = conn.execute('SELECT content FROM comments WHERE post_id=? ORDER BY created_at DESC', (post['id'],))
                            comments = cursor.fetchall()
                            for comment in comments:
                                print(f"- {comment['content']}")
                            print("--------------------")

                    elif user_choice == "3":
                        post_id = int(input("Enter post ID: "))
                        content = input("Enter comment content: ")
                        comment = Comment(conn, post_id, user_id, content)
                        comment.add_comment()

                    elif user_choice == "4":
                        post_id = int(input("Enter post ID: "))
                        like = Like(conn, post_id, user_id)
                        like.add_like()

                    elif user_choice == "5":
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "4":
            cursor = conn.execute('SELECT id, content, created_at FROM posts ORDER BY created_at DESC')
            posts = cursor.fetchall()

            for post in posts:
                print(f"\n{post['created_at']} - {post['content']}")
                print("--------------------")
                print("Comments:")
                cursor = conn.execute('SELECT content FROM comments WHERE post_id=? ORDER BY created_at DESC', (post['id'],))
                comments = cursor.fetchall()
                for comment in comments:
                    print(f"- {comment['content']}")
                print("--------------------")

        elif choice == "5":
            post_id = int(input("Enter post ID: "))
            content = input("Enter comment content: ")
            comment = Comment(conn, post_id, user_id, content)
            comment.add_comment()

        elif choice == "6":
            post_id = int(input("Enter post ID: "))
            like = Like(conn, post_id, user_id)
            like.add_like()

        elif choice == "7":
            print("Exiting...")
            close_connection(conn)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

