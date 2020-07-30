import sqlite3 as sq
from Employee import employee

conn=sq.connect('employee.db')
c=conn.cursor()
'''
c.execute("""create table Employees (empid integer,empnm text,sal integer)""")
'''
def insert_emp(emp):
    with conn:
        c.execute('insert into Employees values(:empid,:empnm,:sal)',
                  {'empid':emp.empid,'empnm':emp.empnm,'sal':emp.sal})
def update_sal(emp,sal):
    with conn:
        c.execute("""update employees set sal=:sal where empid=:empid and empnm=:empnm"""
                  ,{'empid':emp.empid,'empnm':emp.empnm,'sal':sal})
        
def remove_emp(emp):
    with conn:
        c.execute("""Delete from employees where empid=:empid and empnm=:empnm""",
                  {'empid':emp.empid,'empnm':emp.empnm})
        
def search(id_1):
    with conn:
        c.execute("""select * from employees where empid=:empid""",
                  {'empid':id_1})
        temp=c.fetchone()
        
        emp=employee(temp[0],temp[1],temp[2])
        return emp
emp_1=employee(9162809,'vishal',40000)
emp_2=employee(25256,'sam',23455)
'''
insert_emp(emp_1)
insert_emp(emp_2)
'''


#update_sal(emp_1,30000)
'''
remove_emp(emp_2)
remove_emp(emp_1)
'''
emp=search(9162809)
print(emp.empnm)
'''

c.execute('select * from Employees')
print(c.fetchall())

conn.commit()
'''
