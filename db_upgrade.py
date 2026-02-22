import sqlite3

conn = sqlite3.connect("healthcare.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE reports ADD COLUMN prescription_image_path TEXT")
    print("prescription_image_path column added successfully")
except:
    print("Column already exists")

conn.commit()
conn.close()