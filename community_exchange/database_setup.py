import sqlite3


def setup_database():
    conn = sqlite3.connect('community_exchange.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    # Create offers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS offers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        offer TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    # Create comments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        offer_id INTEGER,
        username TEXT,
        comment TEXT,
        FOREIGN KEY (offer_id) REFERENCES offers (id),
        FOREIGN KEY (username) REFERENCES users (username)
    )
    ''')

    # Create ratings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        offer_id INTEGER,
        username TEXT,
        rating INTEGER,
        FOREIGN KEY (offer_id) REFERENCES offers (id),
        FOREIGN KEY (username) REFERENCES users (username)
    )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_database()
