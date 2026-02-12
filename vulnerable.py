import hashlib
import sqlite3
import os
from dotenv import load_dotenv

# Load credentials from environment variables
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_SECRET = os.getenv("API_SECRET")

def authenticate(username, password):
    # Fixed: Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query, (username, password))
    return cursor.fetchone()

def hash_password(password):
    # Fixed: Use strong hashing algorithm (SHA-256 with salt recommended, or bcrypt/argon2)
    import secrets
    salt = secrets.token_hex(16)
    return hashlib.sha256((password + salt).encode()).hexdigest()

def process_input(user_input):
    # Fixed: Avoid command injection by using safe alternatives
    # Instead of os.system, use subprocess with sanitized input
    import subprocess
    # Sanitize input - only allow alphanumeric characters
    if user_input.replace(' ', '').isalnum():
        subprocess.run(['echo', user_input], check=True)
    else:
        raise ValueError("Invalid input: only alphanumeric characters allowed")