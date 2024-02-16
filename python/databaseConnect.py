import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Password@123",
    database = "kunal"
)

mycursor = db.cursor()     
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)
# mycursor.execute("insert into employee (name) values ('abc')")
# db.commit()

# mycursor.execute("select * from employee")
# for x in mycursor:
#     print(x)

# mycursor.execute("update employee set name='kunnu' where name='abc'")

db.commit()

mycursor.execute("delete from employee where name='kunnu'")
db.commit()
mycursor.execute("select * from employee")
for x in mycursor:
    print(x)