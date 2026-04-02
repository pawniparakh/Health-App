import sqlite3

def create_connection():
    return sqlite3.connect("database.db", check_same_thread=False)

def create_tables():
    conn = create_connection()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        aadhaar TEXT UNIQUE,
        password TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_aadhaar TEXT,
        file_name TEXT,
        description TEXT
    )
    ''')

    conn.commit()
    conn.close()

# ➕ Add record
def add_record(aadhaar, file_name, description):
    conn = create_connection()
    c = conn.cursor()

    c.execute("INSERT INTO records (patient_aadhaar, file_name, description) VALUES (?, ?, ?)",
              (aadhaar, file_name, description))

    conn.commit()
    conn.close()

# 📥 Get records
def get_records(aadhaar):
    conn = create_connection()
    c = conn.cursor()

    c.execute("SELECT file_name, description FROM records WHERE patient_aadhaar=?", (aadhaar,))
    data = c.fetchall()

    return data