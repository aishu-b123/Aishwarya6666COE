import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='example'
)
mycursor = mydb.cursor()
create = 'create table sub1 (id int,name varchar(50))'
insert = "INSERT INTO sub1(id,name) VALUES (%s, %s)"
values = [
    ('1', 'Hindi'),
    ('2', 'Telugu'),
    ('3', 'Urdu'),
    ('4','mathematics'),
    ('4','mathematics'),
]
update="update sub1 set name='acd' where id=3"
delete="delete from sub1 where id='2'"

mycursor.execute(create)
mycursor.executemany(insert,values)
mycursor.execute(update)
mycursor.execute(delete)
mydb.commit()
mycursor.close()
mydb.close()