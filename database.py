import sqlite3

# ---------------- CONNECT ----------------
def connect():
    return sqlite3.connect("healthcare.db")


# ---------------- CREATE TABLES ----------------
def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Doctors
    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Patients
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Management
    cur.execute("""
    CREATE TABLE IF NOT EXISTS management(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Reports (FULL VERSION ✅)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_username TEXT,
        doctor_username TEXT,
        patient_name TEXT,
        age INTEGER,
        weight REAL,
        height REAL,
        disease TEXT,
        bp INTEGER,
        sugar INTEGER,
        risk TEXT,
        prescription TEXT,
        signature_path TEXT,
        patient_photo_path TEXT,
        prescription_image_path TEXT,
        visit_time TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- DEFAULT MANAGEMENT ----------------
def create_default_management():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM management WHERE username='admin'")
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO management (username,password) VALUES (?,?)",
            ("admin","admin123")
        )

    conn.commit()
    conn.close()


# ---------------- DOCTOR ----------------
def add_doctor(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO doctors(username,password) VALUES (?,?)",
        (username,password)
    )
    conn.commit()
    conn.close()


def login_doctor(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM doctors WHERE username=? AND password=?",
        (username,password)
    )
    row = cur.fetchone()
    conn.close()
    return row


# ---------------- PATIENT ----------------
def add_patient(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO patients(username,password) VALUES (?,?)",
        (username,password)
    )
    conn.commit()
    conn.close()


def login_patient(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM patients WHERE username=? AND password=?",
        (username,password)
    )
    row = cur.fetchone()
    conn.close()
    return row


# ---------------- MANAGEMENT ----------------
def login_management(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM management WHERE username=? AND password=?",
        (username,password)
    )
    row = cur.fetchone()
    conn.close()
    return row


# ---------------- SAVE REPORT ----------------
def save_report(data):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO reports(
        patient_username,
        doctor_username,
        patient_name,
        age,
        weight,
        height,
        disease,
        bp,
        sugar,
        risk,
        prescription,
        signature_path,
        patient_photo_path,
        prescription_image_path,
        visit_time
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, data)

    conn.commit()
    conn.close()


# ---------------- GET PATIENT REPORTS ----------------
def get_patient_reports(patient_username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT 
        patient_name,age,weight,height,
        disease,bp,sugar,risk,
        prescription,
        signature_path,
        patient_photo_path,
        prescription_image_path,
        visit_time
    FROM reports
    WHERE patient_username=?
    ORDER BY visit_time DESC
    """,(patient_username,))

    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- DOCTOR → PATIENT LIST ----------------
def get_doctor_patients(doctor_username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT DISTINCT patient_username
    FROM reports
    WHERE doctor_username=?
    """,(doctor_username,))

    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- MANAGEMENT MONITOR ----------------
def get_doctor_patient_reports():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT 
        doctor_username,
        patient_username,
        patient_name,
        age,
        disease,
        risk,
        visit_time
    FROM reports
    ORDER BY visit_time DESC
    """)

    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- COUNTS ----------------
def get_total_counts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM doctors")
    d = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM patients")
    p = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM reports")
    r = cur.fetchone()[0]

    conn.close()
    return d,p,r
# ---------------- GET ALL DOCTORS ----------------
def add_doctor(username, password):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM doctors WHERE username=?", (username,))
    if cur.fetchone():
        conn.close()
        return False   # already exists

    cur.execute(
        "INSERT INTO doctors(username,password) VALUES (?,?)",
        (username,password)
    )
    conn.commit()
    conn.close()
    return True


# ---------------- GET ALL PATIENTS ----------------
def add_patient(username, password):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients WHERE username=?", (username,))
    if cur.fetchone():
        conn.close()
        return False   # already exists

    cur.execute(
        "INSERT INTO patients(username,password) VALUES (?,?)",
        (username,password)
    )
    conn.commit()
    conn.close()
    return True

    
    # ---------------- RESET PASSWORD ----------------
def reset_doctor_password(username, new_password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE doctors SET password=? WHERE username=?",
        (new_password, username)
    )
    conn.commit()
    conn.close()


def reset_patient_password(username, new_password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE patients SET password=? WHERE username=?",
        (new_password, username)
    )
    conn.commit()
    conn.close()

def get_all_reports():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT patient_username,
               doctor_username,
               patient_name,
               age,
               disease,
               risk,
               visit_time
        FROM reports
        ORDER BY visit_time DESC
    """)

    rows = cur.fetchall()
    conn.close()
    return rows

    def delete_doctor(username):
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM doctors WHERE username=?", (username,))
        conn.commit()
        conn.close()
        
        def delete_patient(username):
            conn = connect()
            cur = conn.cursor()
            cur.execute("DELETE FROM patients WHERE username=?", (username,))
            conn.commit()
            conn.close()
# ---------------- GET ALL DOCTORS ----------------
def get_all_doctors():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT username FROM doctors")
    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- GET ALL PATIENTS ----------------
def get_all_patients():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT username FROM patients")
    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- RESET DOCTOR PASSWORD ----------------
def reset_doctor_password(username, new_password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE doctors SET password=? WHERE username=?",
        (new_password, username)
    )
    conn.commit()
    conn.close()


# ---------------- RESET PATIENT PASSWORD ----------------
def reset_patient_password(username, new_password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE patients SET password=? WHERE username=?",
        (new_password, username)
    )
    conn.commit()
    conn.close()


# ---------------- DELETE DOCTOR ----------------
def delete_doctor(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM doctors WHERE username=?", (username,))
    conn.commit()
    conn.close()


# ---------------- DELETE PATIENT ----------------
def delete_patient(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE username=?", (username,))
    conn.commit()
    conn.close()
