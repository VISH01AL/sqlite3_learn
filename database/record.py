import sqlite3 as sq
conn=sq.connect('customer.db')

c=conn.cursor()
'''
c.execute("CREATE TABLE customer (first_nm text,last_nm text,email text)")
c.execute("INSERT INTO customer VALUES('Sachin','Tendulkar','abc@gmail.com')")
c.execute("INSERT INTO customer VALUES('Sourab','gangulay','bcd@gmail.com')")
c.execute("INSERT INTO customer VALUES('virat','kholi','efg@gmail.com')")
conn.commit()
'''
'''
c.execute("""update customer set email='sachin@gmail.com' where first_nm='Sachin'""")
c.execute("""update customer set email='virat@gmail.com' where first_nm='virat'""")
c.execute("""update customer set email='sourab@gmail.com' where first_nm='Sourab'""")
'''

'''
c.execute('select * from customer')
items=c.fetchall()

for item in items:
    print(item)
c.execute("""delete from customer where first_nm='virat'""")
'''
c.execute('select * from customer')
items=c.fetchall()

for item in items:
    print(item)
conn.commit()
conn.close()
