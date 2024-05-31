import sqlite3

connection=sqlite3.connect('student.db')
cursor=connection.cursor()
table_info="""

CREATE TABLE student(name TEXT,roll TEXT,section TEXT,marks INT)

"""

cursor.execute(table_info)

cursor.execute("INSERT INTO student VALUES('Rahul','10','A',90)")
cursor.execute("INSERT INTO student VALUES('MOHIT','19','B',80)")
cursor.execute("INSERT INTO student VALUES('RAJ','13','C',70)")
cursor.execute("INSERT INTO student VALUES('POHIT','18','D',60)")

print("Data inserted successfully")

data=cursor.execute("SELECT * FROM student")

for i in data:
    print(i)

connection.commit()
connection.close()