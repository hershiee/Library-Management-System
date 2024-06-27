import mysql.connector as a
con = a.connect(host="localhost", user="root", passwd="1234", database="library")

def addbook():
    bn=input("Enter Book Name :")
    c=input("Enter Book Code :")
    t=input("Total Books :")
    s=input("Enter Subject :")
    data=(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("============================================================================")
    print("Data Entered Successfully")
    main()


def issueb():
    n=input("Enter Name :")
    r=input("Enter Reg No :")
    co=input("Enter Book Code :")
    d=input("Enter Date :")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("=========================================================================")
    print("Book issued to :",n)
    bookup(co,-1)


def submitb():
    n=input("Enter Name :")
    r=input("Enter Reg No :")
    co=input("Enter Book Code :")
    d=input("Enter Date :")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("=========================================================================")
    print("Book submitted from :",n)
    bookup(co,1)

def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myres=c.fetchone()
    t=myres[0]+u
    sql="update books set TOTAL = %s where BCODE = %s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter Book Code :")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a="select * from books"
    c=con.cursor()
    c.execute(a)
    myres=c.fetchall()
    for i in myres:
        print("Book Name :",i[0])
        print("Book Code :",i[1])
        print("Total :",i[2])
        print("Subject :",i[3])
        print("=========================================================================")
    main()
        
        
    
    
    
def main():
    print("""
                          Library Manager
          1. ADD BOOK
          2. ISSUE BOOK
          3. SUBMIT BOOK
          4. DELETE BOOK
          5. DISPLAY BOOKS
          """)
    choice = input("Enter Task No. :")
    print("=========================================================================")
    if(choice=='1'):
              addbook()
    elif(choice=='2'):
              issueb()
    elif(choice=='3'):
              submitb()
    elif(choice=='4'):
               dbook()
    elif(choice=='5'):
              dispbook()
    else:
              print("WRONG CHOICE!...")
              main()
                


def pswd():
    ps=input("Enter Password :")
    if ps=="1234":
        main()
    else:
        print("Wrong Password")
        pswd()


pswd()
