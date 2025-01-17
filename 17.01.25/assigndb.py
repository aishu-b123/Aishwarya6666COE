
import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='example'
)
mycursor = mydb.cursor()

create =''' CREATE TABLE emp (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    JobTitle VARCHAR(50),
    HireDate DATE,
    Salary DECIMAL(10, 2)
)'''
insert=''' INSERT INTO emp (EmployeeID, FirstName, LastName, Department, JobTitle, HireDate, Salary) VALUES (%s, %s,%s,%s,%s,%s,%s) '''
values=[
(1, 'John', 'Doe', 'Sales', 'Sales Manager', '2020-05-15', 75000.00),
(2, 'Jane', 'Smith', 'Marketing', 'Marketing Specialist', '2021-03-10', 62000.00),
(3, 'Michael', 'Johnson', 'IT', 'System Administrator', '2018-07-22', 82000.00),
(4, 'Emily', 'Brown', 'HR', 'HR Coordinator', '2019-12-05', 55000.00),
(5, 'Chris', 'Davis', 'Sales', 'Sales Representative', '2017-08-11', 67000.00),
(6, 'Sarah', 'Martinez', 'Marketing', 'Content Creator', '2022-01-17', 54000.00),
(7, 'David', 'Taylor', 'IT', 'Software Engineer', '2016-02-25', 95000.00),
(8, 'Linda', 'Harris', 'Finance', 'Financial Analyst', '2018-06-18', 78000.00),
(9, 'James', 'Clark', 'Operations', 'Operations Manager', '2014-04-03', 88000.00),
(10, 'Olivia', 'Lewis', 'HR', 'Recruiter', '2023-08-19', 51000.00),
(11, 'Daniel', 'Walker', 'Sales', 'Sales Executive', '2021-09-29', 74000.00),
(12, 'Sophia', 'Young', 'Marketing', 'SEO Specialist', '2020-10-14', 59000.00),
(13, 'Matthew', 'King', 'Finance', 'CFO', '2010-11-30', 150000.00),
(14, 'Ava', 'Wright', 'IT', 'Network Engineer', '2017-02-10', 72000.00),
(15, 'Ethan', 'Scott', 'Operations', 'Warehouse Supervisor', '2015-01-09', 67000.00)
]
display="select * from emp where department='IT'"

update_salary = "UPDATE emp SET Salary = %s WHERE EmployeeID = %s"

delete_employee = "DELETE FROM emp WHERE EmployeeID = %s"

count_department = "SELECT Department, COUNT(*) FROM emp GROUP BY Department"

select_salary_above = "SELECT * FROM emp WHERE Salary > %s"

sort_salary = "SELECT * FROM emp ORDER BY Salary DESC"

mycursor.execute(create)
mycursor.executemany(insert,values)
mycursor.execute(display)
res=mycursor.fetchall()
for row in res:
    print(row)

sal=80000
id=4
mycursor.execute(update_salary,(sal,id))

del_id = 5
mycursor.execute(delete_employee,(del_id,))

mycursor.execute(count_department)
res = mycursor.fetchall()
for row in res:
    print(f"Department: {row[0]}, Number of Employees: {row[1]}")

mydb.commit()
mycursor.close()
mydb.close()