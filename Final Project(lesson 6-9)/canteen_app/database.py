import hashlib
import secrets
import sqlite3
from pathlib import Path
from translator import translate

ALLERGENS = ["celery", "gluten", "crustaceans", "eggs", "fish", "lupin", "milk",
             "molluscs", "mustard", "tree nuts", "peanuts", "sesame", "soya", "sulphites"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS meals (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS allergens (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, salt TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('staff', 'student')),
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS student_allergens (
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    allergen_id INTEGER REFERENCES allergens(id),
    PRIMARY KEY (student_id, allergen_id)
);

CREATE TABLE IF NOT EXISTS meal_allergens (
    meal_id INTEGER REFERENCES meals(id) ON DELETE CASCADE,
    allergen_id INTEGER REFERENCES allergens(id),
    PRIMARY KEY (meal_id, allergen_id)
);

CREATE TABLE IF NOT EXISTS assignments (
    student_id INTEGER PRIMARY KEY REFERENCES students(id) ON DELETE CASCADE,
    meal_id INTEGER REFERENCES meals(id) ON DELETE CASCADE
);
"""

def connect(path=None, demo=True):
    if(path is None) :
        folder = Path.home() #./canteen_app
        folder.mkdir(exist_ok=True)
        path = folder / "canteen.db"
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    if(conn.execute("SELECT COUNT(*) FROM allergens").fetchone()[0] == 0):
        for name in ALLERGENS:
            conn.execute("INSERT INTO allergens (name) VALUES(?)", (name,))
        if demo:
            add_demo_data(conn)
        conn.commit()
    return conn


def add_demo_data(conn):
    add(conn, "meal", "Pasta Bake", ["gluten", "milk"])
    add(conn, "meal", "Chicken Satay", ["peanuts", "soya"])
    add(conn, "meal", "Fish and Chips", ["fish", "gluten"])
    add(conn, "meal", "Vegetable Curry", ["mustard"])
    ali = add(conn, "student", "Ali Yusifzade", ["peanuts"])
    muradkhan = add(conn, "student", "Muradkhan Mammadov", ["milk"])
    add(conn, "student", "Nigar Mammadova", ["gluten"])
    add(conn, "student", "Aysha Sardarova", [])
    add(conn, "student", "Tuncay Alakbarly", ["gluten", "peanuts", "mustard"])
    add_user(conn, "admin", "admin123", "staff")
    add_user(conn, "ali", "ali123", "student", ali)
    add_user(conn, "muradkhan", "muradkhan123", "student", muradkhan)


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 100_000).hex()


def add_user(conn, username, password, role, student_id=None):
    salt = secrets.token_hex(16)
    conn.execute("INSERT INTO users (username, password_hash, salt, role, student_id) VALUES (?, ?, ?, ?, ?)",
                 (username, hash_password(password, salt), salt, role, student_id))
    conn.commit


def login(conn, username, password):
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if user and secrets.compare_digest(hash_password(password, user["salt"]), user["password_hash"]):
        return user
    return None


def add(conn, kind, name, allergens):
    name = name.strip()
    if(not name):
        raise ValueError(translate("err.empty"))
    try:
        new_id = conn.execute(f"INSERT INTO {kind}s (name) VALUES (?)", (name,)).lastrowid
    except sqlite3.IntegrityError:
        raise ValueError(translate("err.exists")) from None
    
    for allergen in allergens:
        conn.execute(f"INSERT INTO {kind}_allergens ({kind}_id, allergen_id) "
                     "SELECT ?, id FROM allergens WHERE name = ?", (new_id, allergen))
        
    conn.commit()
    return new_id


def allergens_of(conn, kind, row_id):
    rows = conn.execute(f"SELECT a.name FROM {kind}_allergens x JOIN allergens a ON a.id = x.allergen_id"
                        f"WHERE x.{kind}_id = ?", (row_id,))
    row_names = []
    for row in rows:
        row_names.append(row["name"])

    return row_names


def list_all(conn, kind):
    return conn.execute(f"SELECT * FROM {kind}s ORDER BY name").fetchall()


def assigned_meal(conn, student_id):
    return conn.execute("SELECT m.* FROM assignments a JOIN meals m ON m.id = a.meal_id"
                        "WHERE a.student_id = ?", (student_id)).fetchone()


def save_assignment(conn, student_id, meal_id):
    conn.execute("INSERT OR REPLACE INTO assignments (student_id, meal_id) VALUES(?, ?)", (student_id, meal_id))
    conn.commit()