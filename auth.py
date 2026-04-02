import hashlib
from utils import create_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, aadhaar, password):
    conn = create_connection()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO patients (name, aadhaar, password) VALUES (?, ?, ?)",
                  (name, aadhaar, hash_password(password)))
        conn.commit()
        return True
    except:
        return False

def login_user(aadhaar, password):
    conn = create_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM patients WHERE aadhaar=? AND password=?",
              (aadhaar, hash_password(password)))

    return c.fetchone()