import sqlite3


conn = sqlite3.connect('filesdb/ourusers.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(id INT); ")


def add(id):
    if (id,) in get_id(): return
    cur.execute(f"INSERT INTO users VALUES({id});")
    conn.commit()

def get_all():
    s = cur.execute("SELECT * FROM users;").fetchall()
    conn.commit()
    return s

def count():
    s = cur.execute("SELECT COUNT(*) FROM users;").fetchone()
    conn.commit()
    return s[0]

def get_id():
    s = cur.execute("SELECT id FROM users;").fetchall()
    conn.commit()
    return s

