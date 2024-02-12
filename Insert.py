import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'BOB KURIA',32,245000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JANE MUTHONI',27,145000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'GLORY GRACE',29,145000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'JUNE MUMO',38,300000.00)")

conn.commit()

print("Records inserted successfully")
conn.close()
