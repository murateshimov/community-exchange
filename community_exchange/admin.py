from person import Person
import sqlite3


class Admin(Person):
    def __init__(self, username, password, name):
        super().__init__(username, password, name)

    def view_users(self):
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('SELECT username, name, role FROM users')
        users = cursor.fetchall()
        conn.close()
        return users

    def delete_user(self, username):
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE username=?', (username,))
        conn.commit()
        conn.close()

    def view_offers(self):
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, user_id, offer FROM offers')
        offers = cursor.fetchall()
        conn.close()
        return offers

    def delete_offer(self, offer_id):
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM offers WHERE id=?', (offer_id,))
        conn.commit()
        conn.close()
