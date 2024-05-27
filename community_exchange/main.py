import sqlite3
from person import Person
from user import User
from admin import Admin
from contributor import Contributor
from partner import Partner


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


def user_menu(user):
    while True:
        print("\nUser Menu:")
        print("1. Publish Offer")
        print("2. View Offers")
        print("3. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            offer = input("Enter the offer description: ")
            user.publish_offer(offer)
            print("Offer published successfully.")
        elif choice == '2':
            offers = user.view_offers()
            print("\nOffers:")
            for offer in offers:
                print(f"- {offer}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. View Users")
        print("2. Delete User")
        print("3. View Offers")
        print("4. Delete Offer")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            users = admin.view_users()
            print("\nUsers:")
            for user in users:
                print(f"Username: {user[0]}, Name: {user[1]}, Role: {user[2]}")
        elif choice == '2':
            username = input("Enter the username to delete: ")
            admin.delete_user(username)
            print(f"User {username} deleted successfully.")
        elif choice == '3':
            offers = admin.view_offers()
            print("\nOffers:")
            for offer in offers:
                print(
                    f"ID: {offer[0]}, User ID: {offer[1]}, Offer: {offer[2]}")
        elif choice == '4':
            offer_id = input("Enter the offer ID to delete: ")
            admin.delete_offer(offer_id)
            print(f"Offer ID {offer_id} deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def contributor_menu(contributor):
    while True:
        print("\nContributor Menu:")
        print("1. Publish Material")
        print("2. Comment on Offer")
        print("3. Rate Offer")
        print("4. View Offers")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            material = input("Enter the material: ")
            contributor.publish_material(material)
        elif choice == '2':
            offer_id = input("Enter the offer ID to comment on: ")
            comment = input("Enter your comment: ")
            contributor.comment_on_offer(offer_id, comment)
        elif choice == '3':
            offer_id = input("Enter the offer ID to rate: ")
            rating = int(input("Enter your rating (1-5): "))
            contributor.rate_offer(offer_id, rating)
        elif choice == '4':
            offers = contributor.view_offers()
            if isinstance(offers, list):
                for offer in offers:
                    print(
                        f"Offer ID: {offer[0]}, User ID: {offer[1]}, Description: {offer[2]}")
            else:
                print(offers)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def partner_menu(partner):
    while True:
        print("\nPartner Menu:")
        print("1. Provide Support")
        print("2. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            new_user = input("Enter the new user's username to support: ")
            partner.provide_support(new_user)
            print("Support provided successfully.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\nWelcome to the Community Exchange Platform")
        print("1. Login")
        print("2. Register")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_data = authenticate_user(username, password)
            if user_data:
                print(f"Welcome {user_data[3]}")  # user_data[3] is the name
                role = user_data[4]
                if role == 'user':
                    user = User(
                        username=user_data[1], password=user_data[2], name=user_data[3])
                    user_menu(user)
                elif role == 'admin':
                    admin = Admin(
                        username=user_data[1], password=user_data[2], name=user_data[3])
                    admin_menu(admin)
                elif role == 'contributor':
                    contributor = Contributor(
                        username=user_data[1], password=user_data[2], name=user_data[3])
                    contributor_menu(contributor)
                elif role == 'partner':
                    partner = Partner(
                        username=user_data[1], password=user_data[2], name=user_data[3])
                    partner_menu(partner)
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
