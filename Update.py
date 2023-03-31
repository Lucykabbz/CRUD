import sqlite3

conn = sqlite3.connect('Companyy.db')
print("Successfully connected to the database")

conn.execute("UPDATE Company1 set Salary = 50000.00 WHERE ID= 11")
conn.commit()

data = conn.execute("SELECT * FROM Company1")
for rows in data:
    print("ID:", rows[0])
    print("FIRSTNAME:", rows[1])
    print("LASTNAME:", rows[2])
    print("AGE:", rows[3])
    print("SALARY:", rows[4])
    print("TASK:", rows[5])

print("Successfully removed one row")

conn.close()




