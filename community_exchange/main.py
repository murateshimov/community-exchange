import sqlite3
from person import Person


def register_user(username, password, name, role):
    conn = sqlite3.connect('community_exchange.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password, name, role) VALUES (?, ?, ?, ?)',
                       (username, password, name, role))
        conn.commit()
        print(f"User {name} registered successfully as {role}")
    except sqlite3.IntegrityError:
        print("Error: Username already exists")
    finally:
        conn.close()


def authenticate_user(username, password):
    conn = sqlite3.connect('community_exchange.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user


def main():
    while True:
        print("Welcome to the Community Exchange Platform")
        print("1. Login")
        print("2. Register")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = authenticate_user(username, password)
            if user:
                print(f"Welcome {user[3]}")  # user[3] is the name
                # Show menu based on user role
                # Placeholder for future role-based menu
                print(f"Logged in as {user[4]}")  # user[4] is the role
            else:
                print("Invalid username or password")

        elif choice == '2':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            name = input("Enter your name: ")
            role = input(
                "Enter your role (user, admin, contributor, partner): ")

            register_user(username, password, name, role)


if __name__ == "__main__":
    main()
