import sqlite3

conn = sqlite3.connect('Companyy.db')

conn.execute("INSERT INTO Company1( ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
             VALUES (11, 'Andrew', 'Allan', 21, 30000.00, 'Manager')");
conn.execute("INSERT INTO Company1( ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
             VALUES (12, 'Amelia', 'Roy', 31, 36000.00, 'Treasurer')");
conn.execute("INSERT INTO Company1( ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
             VALUES (13, 'Faith', 'Smart', 25, 40000.00, 'Clerk')");
conn.execute("INSERT INTO Company1( ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
             VALUES (15, 'Bernard', 'Allan', 26, 60000.00, 'Secretary')");
conn.execute("INSERT INTO Company1( ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
             VALUES (16, 'Ryan', 'Alihay', 23, 16000.00, 'Cleaner')");

conn.commit()
print("Successfully Inserted values in Company1 table")

conn.close()
