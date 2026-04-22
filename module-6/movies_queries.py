import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="student",
    password="password123",
    database="movies"
)

cursor = db.cursor()

print("\n-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT * FROM studio")
for studio in cursor.fetchall():
    print(studio)

print("\n-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT * FROM genre")
for genre in cursor.fetchall():
    print(genre)

print("\n-- DISPLAYING Short Films (under 2 hours) --")
cursor.execute("SELECT name FROM film WHERE runtime < 120")
for film in cursor.fetchall():
    print(film)

print("\n-- DISPLAYING Films Grouped by Director --")
cursor.execute("SELECT name, director FROM film ORDER BY director")
for film in cursor.fetchall():
    print(film)

db.close()
