# database.py

import sqlite3
from contextlib import closing
from config import DB_PATH

# Inicializa la base de datos y las tablas
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            # Tabla de mensajes automáticos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    enabled INTEGER DEFAULT 1,
                    interval_min INTEGER DEFAULT 60,
                    interval_max INTEGER DEFAULT 300
                );
            """)
            # Tabla de usuarios (chat_id)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chat_id INTEGER UNIQUE
                );
            """)
            conn.commit()

# ==========================
# MENSAJES AUTOMÁTICOS
# ==========================

def add_message(content, interval_min=60, interval_max=300):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                INSERT INTO messages (content, interval_min, interval_max)
                VALUES (?, ?, ?);
            """, (content, interval_min, interval_max))
            conn.commit()

def get_all_messages():
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("SELECT * FROM messages;")
            return cursor.fetchall()

def update_message(id, content, interval_min, interval_max):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                UPDATE messages
                SET content = ?, interval_min = ?, interval_max = ?
                WHERE id = ?;
            """, (content, interval_min, interval_max, id))
            conn.commit()

def set_message_status(id, enabled):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                UPDATE messages SET enabled = ? WHERE id = ?;
            """, (1 if enabled else 0, id))
            conn.commit()

def delete_message(id):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("DELETE FROM messages WHERE id = ?;", (id,))
            conn.commit()

# ==========================
# MANEJO DE USUARIOS
# ==========================

def get_message_by_id(msg_id):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("SELECT id, content, enabled, interval_min, interval_max FROM messages WHERE id = ?", (msg_id,))
            return cursor.fetchone()

def save_chat_id(chat_id):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                INSERT OR IGNORE INTO users (chat_id) VALUES (?);
            """, (chat_id,))
            conn.commit()

def get_all_chat_ids():
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("SELECT chat_id FROM users;")
            return [row[0] for row in cursor.fetchall()]

def delete_chat_id(chat_id):
    with sqlite3.connect(DB_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("DELETE FROM users WHERE chat_id = ?;", (chat_id,))
            conn.commit()
