import sqlite3


def delete_data():
    """Delete all data from all tables in the database."""
    conn = sqlite3.connect(
        'community_exchange.db')  # Ensure the database name matches your setup
    cur = conn.cursor()
    # Adjust the table names as necessary. These should match your actual table names
    cur.execute("DELETE FROM users")  # Assuming 'users' is one of your tables
    cur.execute("DELETE FROM offers")  # Assuming 'offers' is another table
    # Add more tables if you have them
    conn.commit()
    conn.close()
    print("All data deleted successfully")


if __name__ == '__main__':
    delete_data()
