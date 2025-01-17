import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='example'
)
mycursor = mydb.cursor()
#sql='select * from customer'
#sql = 'create table aiml (id int,name varchar(50),address varchar(50))'
#sql="insert into aiml values(1,'aish','warangal')"
#sql="update aiml set name='aishwarya' where id=1"
'''sql='delete from aiml where id=1'
mycursor.execute(sql)
results = mycursor.fetchall()
for row in results:
    print(row)'''
name=input("Enter your name:")
id = input("Enter your id:")
address=input('enter the address:')
mycursor.execute("insert into aiml values(%s,%s,%s)",(id,name,address))
mydb.commit()
mydb.commit()
mycursor.close()
mydb.close()