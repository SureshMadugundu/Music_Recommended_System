import mysql.connector as con
db=con.connect(host="localhost",user="sqluser",password="Admin@3212#",database="student")

cur=db.cursor()
cur.execute("create database Ram")
print("created")
