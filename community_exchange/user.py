import sqlite3
from person import Person


class User(Person):
    def __init__(self, username, password, name):
        super().__init__(username, password, name)

    def publish_offer(self, offer):
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO offers (user_id, offer) VALUES ((SELECT id FROM users WHERE username=?), ?)', (self.username, offer))
        conn.commit()
        conn.close()

    def view_offers(self):
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('SELECT offer FROM offers')
        offers = cursor.fetchall()
        conn.close()
        return [offer[0] for offer in offers]
