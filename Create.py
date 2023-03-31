import sqlite3

conn = sqlite3.connect('Companyy.db')
print("Successfully opened database")

conn.execute("""CREATE TABLE Company1(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE int,
Salary REAL,
TASK TEXT CHAR(20))""")

print("Successfully Created Company1table")
conn.close()
