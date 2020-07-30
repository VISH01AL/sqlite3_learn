import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def accexist(accno,c):
    c.execute("""select accno from customer where accno=:accno""",{'accno':accno})
    li=c.fetchone()
    if li:
        return True
    else:
        return False
def option1():
    with conn:
            c=conn.cursor()
            accno=None
            fname=None
            lname=None
            bal=None
            try:
                accno=int(input('enter accno:'))
                fname=input('enter fname:')
                lname=input('enter lname:')
                bal=int(input('enter first time deposit:'))
            except:
                print("<<<please entet valid details>>>")
                return
            
            if not accexist(accno,c):
                c.execute("""Insert into customer values(:accno,:fname,:lname,:bal)""",
                        {'accno':accno,'fname':fname,'lname':lname,'bal':bal})
                conn.commit()
                print("<<<transcation successful>>>")
            else:
                print("<<<accno is taken please enter another unique accno>>>")
def option2():
    with conn:
        c=conn.cursor()
        accno=None
        try:
            accno=int(input('enter accno:'))
            dep=int(input('enter deposit amount:'))
            if dep<0:
                print("please enter positive deposit")
                return
        except:
            print("<<<please enter valid details>>>")
            return
        c.execute("""select bal from customer where accno=:accno""",{'accno':accno})
        li=c.fetchall()
        if len(li)==0:
            print("<<<accno not found please enter a valid accno>>>")
        else:
            c.execute("""update customer set bal=:bal where accno=:accno""",
                      {'bal':li[0][0]+dep,'accno':accno})
            conn.commit()
            print("<<<transcation successful>>>")
def option3():
    with conn:
        c=conn.cursor()
        accno=None
        try:
            accno=int(input('enter accno:'))
            wit=int(input('enter withdrawl amount:'))
            if wit<0:
                print("<<<please enter positive withdraw>>>")
                return
        except:
            print("<<<please enter valid details>>>")
            return
        c.execute("""select bal from customer where accno=:accno""",{'accno':accno})
        li=c.fetchall()
        if li[0][0]<wit:
            print("<<<you don't have sufficient balance>>>")
            print("<<<your balance is:",li[0][0],">>>")
            return
        if len(li)==0:
            print("<<<accno not found please enter a valid accno>>>")
        else:
            c.execute("""update customer set bal=:bal where accno=:accno""",
                      {'bal':li[0][0]-wit,'accno':accno})
            conn.commit()
            print("<<<transcation successful>>>")
def option4():
    with conn:
        c=conn.cursor()
        try:
            accno=int(input('enter your accno:'))
        except:
            print("<<<please enter a valid accno>>>")
        c.execute("select bal from customer where accno=:accno",
                  {'accno':accno})
        li=c.fetchall()
        if len(li)==0:
            print('<<<please enter a valid accno>>>')
        else:
            print("the accno balance is:",li[0][0])
            print("<<<transcation successful>>>")
def option5():
    with conn:
        c=conn.cursor()
        c.execute("select * from customer")
        li=c.fetchall()
        print("accno   fname   lname    balance")
        for x in li:
            print(x)
        print("<<<transcation successful>>>")
def option6():
    with conn:
        c=conn.cursor()
        accno=None
        try:
            accno=int(input('enter your accno to be deleted:'))
        except:
            print("<<<please enter a valid accno>>>")
        if accexist(accno,c):
            c.execute("""Delete from customer where accno=:accno""",
                      {'accno':accno})
            conn.commit()
            print("<<<account deleted>>>")
        else:
            print("<<<account could not be found>>>")
def option7():
    with conn:
        c=conn.cursor()
        accno=None
        fname=None
        lname=None
        bal=None
        try:
            accno=int(input('enter your accno:'))
            fname=input('enter fname for update:')
            lname=input('enter lname for update:')
            bal=int(input('enter new balance:'))
        except:
            print("<<<please enter a valid accno>>>")
        if not accexist(accno,c):
            print("<<<accno does not exist>>>")
        else:
            c.execute("""select * from customer where accno=:accno""",{'accno':accno})
            li=c.fetchone()
            c.execute("""update customer set fname=:fname,lname=:lname,bal=:bal where accno=:accno""",
                      {'fname':fname,'lname':lname,'bal':bal,'accno':accno})
            conn.commit()
            print("<<<account details updated from",li,"to",fname," ",lname," ",bal,">>>")
            print("transaciton completed")
def main():
    print("WELCOME TO BANK")
    while True:
        print("press an number")
        print("NEW ACCOUNT-1")
        print("DEPOSIT AMOUNT-2")
        print("WITHDRAW AMOUNT-3")
        print("BALANCE ENQUIRY-4")
        print("ALL ACCOUNT HOLDER LIST-5")
        print("CLOSE AN ACCOUNT-6")
        print("MODIFY AN ACCOUNT-7")
        print("EXIT-8")
        option=None
        try:
            option=int(input())
        except:
            print("--------------please enter a valid option------------")
        if option>8:
            print("--------------please enter a valid option------------")
            continue
        elif option==1:
            option1()  
        elif option==2:
            option2()
        elif option==3:
            option3()
        elif option==4:
            option4()
        elif option==5:
            option5()
        elif option==6:
            option6()
        elif option==7:
            option7()
        else:
            break

if __name__=='__main__':
    #used for first time creation of database and table
    '''
    conn=create_connection('Customer.db')
    c=conn.cursor()
    c.execute("create table customer (accno integer,fname text,lname text,bal integer)")
    conn.commit()
    conn.close()
    '''
    conn=create_connection('Customer.db')
    main()
    #to show all the data in tables
    '''
    with conn:
        c=conn.cursor()
        c.execute("select * from customer")
        print(c.fetchall())
    '''
