import mysql.connector

conn = None

def connect():
    global conn
    if conn is None or not conn.is_connected():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="actowiz",
            database="Burger_king"   # YOUR DATABASE NAME
        ) 
    return conn


# FOR CREATE TABLE
def create(table_name: str):
    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            restarent_id VARCHAR(50) NOT NULL,
            restaurant_name VARCHAR(255),
            slug VARCHAR(255),
            address VARCHAR(255),
            phone_number VARCHAR(50),
            hours TEXT
        );"""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

""" WITHOUT BATCHES DATABASE FOR SINGLE FILE """
def insert_into_db(table_name: str, data: dict):
    cols = ",".join(list(data.keys()))
    vals = ",".join(['%s'] * len(data.keys()))
    query = f"""INSERT IGNORE INTO {table_name} ({cols}) VALUES ({vals})"""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, tuple(data.values()))
    conn.commit()


if __name__ == "__main__":
    connect()
    print("DB connection OK")   