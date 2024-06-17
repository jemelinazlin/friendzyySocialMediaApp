from colorama import init, Fore, Style
from database.connection import get_db_connection, create_tables, close_connection
from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like

# Initialize colorama to support ANSI colors on Windows
init()

def display_welcome_message():
    print(Fore.CYAN + "Welcome to Friendzyy!")
    print("Friendzyy is a social media app where you can connect with friends, share posts,")
    print("comment on posts, and like posts.")
    print("Let's get started!" + Style.RESET_ALL)

def main():
    conn = get_db_connection()

    create_tables(conn)

    display_welcome_message()

    while True:
        print("\nMenu:")
        print(Fore.YELLOW + "1. Sign up")
        print("2. Log in")
        print("3. Create post")
        print("4. View feed")
        print("5. Add comment")
        print("6. Add like")
        print("7. Exit" + Style.RESET_ALL)

        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == "1":
            username = input(Fore.GREEN + "Enter username: " + Style.RESET_ALL)
            password = input(Fore.GREEN + "Enter password: " + Style.RESET_ALL)
            user = User(conn, username, password)
            user.sign_up()

        elif choice == "2":
            username = input(Fore.GREEN + "Enter username: " + Style.RESET_ALL)
            password = input(Fore.GREEN + "Enter password: " + Style.RESET_ALL)
            user = User(conn, username, password)
            user_id = user.log_in()
            if user_id:
                while True:
                    print("\nUser menu:")
                    print(Fore.YELLOW + "1. Create post")
                    print("2. View feed")
                    print("3. Add comment")
                    print("4. Add like")
                    print("5. Log out" + Style.RESET_ALL)

                    user_choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

                    if user_choice == "1":
                        content = input(Fore.GREEN + "Enter post content: " + Style.RESET_ALL)
                        image_url = input(Fore.GREEN + "Enter image URL (optional, press Enter to skip): " + Style.RESET_ALL)
                        post = Post(conn, user_id, content, image_url=image_url)
                        post.create_post()

                    elif user_choice == "2":
                        # View feed
                        Post.view_feed(conn, user_id)

                    elif user_choice == "3":
                        post_id = int(input(Fore.GREEN + "Enter post ID: " + Style.RESET_ALL))
                        content = input(Fore.GREEN + "Enter comment content: " + Style.RESET_ALL)
                        comment = Comment(conn, post_id, user_id, content)
                        comment.add_comment()

                    elif user_choice == "4":
                        post_id = int(input(Fore.GREEN + "Enter post ID: " + Style.RESET_ALL))
                        like = Like(conn, post_id, user_id)
                        like.add_like()

                    elif user_choice == "5":
                        break

                    else:
                        print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

        elif choice == "4":
            # View global feed
            Post.view_global_feed(conn)

        elif choice == "5":
            post_id = int(input(Fore.GREEN + "Enter post ID: " + Style.RESET_ALL))
            content = input(Fore.GREEN + "Enter comment content: " + Style.RESET_ALL)
            comment = Comment(conn, post_id, user_id, content)
            comment.add_comment()

        elif choice == "6":
            post_id = int(input(Fore.GREEN + "Enter post ID: " + Style.RESET_ALL))
            like = Like(conn, post_id, user_id)
            like.add_like()

        elif choice == "7":
            print(Fore.CYAN + "Exiting..." + Style.RESET_ALL)
            close_connection(conn)
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
