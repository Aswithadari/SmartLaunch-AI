import sqlite3
from datetime import datetime

DB_NAME = "history.db"

def init_db():
    """Initializes the database and creates the schema if it doesn't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS uploads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                project_name TEXT,
                tech_stack TEXT,
                file_count INTEGER
            )
        ''')
        conn.commit()

def log_upload(project_name, tech_stack, file_count):
    """Inserts a new analysis record into the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO uploads (timestamp, project_name, tech_stack, file_count)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, project_name, tech_stack, file_count))
        conn.commit()

def get_recent_history(limit=5):
    """Fetches the latest records for the sidebar."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT timestamp, project_name, tech_stack FROM uploads ORDER BY id DESC LIMIT ?', (limit,))
        return cursor.fetchall()