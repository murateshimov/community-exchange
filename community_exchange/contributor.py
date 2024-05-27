from person import Person
import sqlite3


class Contributor(Person):
    def __init__(self, username, password, name):
        super().__init__(username, password, name)

    def publish_material(self, material):
        # Logic to publish materials
        print(f"Material published: {material}")
        pass

    def comment_on_offer(self, offer_id, comment):
        # Logic to comment on offers
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO comments (offer_id, username, comment) VALUES (?, ?, ?)',
                       (offer_id, self.username, comment))
        conn.commit()
        conn.close()
        pass

    def rate_offer(self, offer_id, rating):
        # Logic to rate offers
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ratings (offer_id, username, rating) VALUES (?, ?, ?)',
                       (offer_id, self.username, rating))
        conn.commit()
        conn.close()
        pass

    def view_offers(self):
        # Retrieve and display all offers from the database
        conn = sqlite3.connect('community_exchange.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, user_id, offer FROM offers")
        offers = cursor.fetchall()
        conn.close()
        if offers:
            return offers
        else:
            return "No offers available."
