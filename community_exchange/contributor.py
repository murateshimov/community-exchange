from person import Person
import sqlite3


class Contributor(Person):
    def __init__(self, username, password, name):
        super().__init__(username, password, name)

    def publish_material(self, material):
        # Logic to publish materials
        print(f"Material published: {material}")

    def comment_on_offer(self, offer_id, comment):
        # Logic to comment on offers
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO comments (offer_id, username, comment) VALUES (?, ?, ?)',
                       (offer_id, self.username, comment))
        conn.commit()
        conn.close()

    def rate_offer(self, offer_id, rating):
        # Logic to rate offers
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ratings (offer_id, username, rating) VALUES (?, ?, ?)',
                       (offer_id, self.username, rating))
        conn.commit()
        conn.close()
