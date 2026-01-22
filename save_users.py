from sqlite3 import connect

location = 'user_db.db'
def create_user():
    with connect(location) as conn:
        cursor = conn.cursor()
        # cursor.execute(
        #     """
        #     Drop TABLE IF EXISTS users;
        #     """
        # )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                name TEXT,
                start_time TEXT DEFAULT (datetime('now')),
                username TEXT
            );
            """
        )
        conn.commit()

def insert_user(telegram_id, name, username):
    with connect(location) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO users (telegram_id, name, username) VALUES (?,?,?);
            """,
            (telegram_id,name,username)
        )
        conn.commit()

def get_user():
    with connect(location) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM users;
            """
        )
        rows = cursor.fetchall()
        return rows
