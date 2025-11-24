# check_user_flags.py
import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute("SELECT id, email, is_active, is_verified FROM user")
rows = c.fetchall()
for r in rows:
    print(r)
conn.close()
