import sqlite3 # importing sqlite library for python 3.* versions

connection = sqlite3.connect("students.db") # connecting to database

print("Database connected!")

cursor = connection.cursor() # object to manipulate database

# Creating 
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birth_year INTEGER,
    city TEXT
)
""")


print("Changes executed!")


# # Inserting
# cursor.execute("""
# INSERT INTO students (name, birth_year, city)
# VALUES ('Fuad', 2009, 'Ganja')
# """
# )

# Selecting
cursor.execute("SELECT * FROM students") # '*' = everything
students = cursor.fetchall() # fetch - get, obrain
print(students)

# Selecting by COLUMN
cursor.execute("SELECT name FROM students")
students = cursor.fetchall()
print(students)

# Selecting by sorting(WHERE) 
cursor.execute("""
SELECT * FROM students 
WHERE city = 'Sumqayit'
""") # WHERE - sorting
students = cursor.fetchall()
print(f"Students from baku: {students}")

# cursor.execute("""
# UPDATE students
# SET name = 'Ilham'
# WHERE id = 1
# """)# SET - setting data to sorted row


# Deleting
cursor.execute("""
DELETE FROM students
WHERE name = 'Ali'               
""")
connection.commit() # commiting changes(saving in database)""
