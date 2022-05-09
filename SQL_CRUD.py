import pymysql as p
def getconnect():
    return p.connect(host="localhost",user="root",password="",database="dbassign")

def InsertData(t):
    db=getconnect()
    sql="insert into emp values(%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Data Inserted Successfully.......!")
    db.commit()
    db.close()

def ShowDetails():
    db=getconnect()
    sql="select * from emp"
    cr=db.cursor()
    cr.execute(sql)
    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^5} {d[1]:^10} {d[2]:^20} {d[3]:^10}")

    db.commit()
    db.close()

def Show_Name(t):
    db=getconnect()
    sql="select name from emp where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^10}")

    db.commit()
    db.close()

def Show_Dept(t):
    db=getconnect()
    sql="select dept from emp where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^20}")

    db.commit()
    db.close()

def Show_Sal(t):
    db=getconnect()
    sql="select salary from emp where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^10}")

    db.commit()
    db.close()

def Update_Dept(t):
    db=getconnect()
    sql="update emp set dept=%s where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Department Updated Successfully.......!")
    db.commit()
    db.close()

def Update_Name(t):
    db=getconnect()
    sql="update emp set name=%s where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Name Updated Successfully.....!")
    db.commit()
    db.close()

def Update_Sal(t):
    db=getconnect()
    sql="update emp set salary=%s where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Salary Updated Successfully.....!")
    db.commit()
    db.close()

def Update_Details(t):
    db=getconnect()
    sql="update emp set name=%s,dept=%s,salary=%s where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Details Updated Successfully......!")
    db.commit()
    db.close()

def Delete_Dept(t):
    db=getconnect()
    sql="update emp set dept=NULL where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Data Deleted Successfully.....!")
    db.commit()
    db.close()

def Delete_Sal(t):
    db=getconnect()
    sql="update emp set salary=NULL where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Data Deleted Successfully.....!")
    db.commit()
    db.close()

def Delete_Name(t):
    db=getconnect()
    sql="update emp set name=NULL where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Data Deleted Successfully.....!")
    db.commit()
    db.close()

def DeleteData(t):
    db=getconnect()
    sql="delete from emp where id=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    print("Data Deleted Successfully.....!")
    db.commit()
    db.close()


while(True):

    print('''
        Database Operations:
        To Insert Records, Press 1
        To Update Records, Press 2
        To Delete Records, Press 3
        To View Records, Press 4
        To Exit, Press 5
        ''')

    operation=int(input("Proceed:"))

    if(operation==1):
        ids=int(input("Enter Id Number:"))
        Name=input("Enter Name:")
        Department=input("Enter Department:")
        Salary=float(input("Enter Salary:"))

        t=(ids,Name,Department,Salary)
        InsertData(t)

    elif(operation==2):
        print('''
            To Update Name, Press 1
            To Update Department, Press 2
            To Update Salary, Press 3
            To Update All Details, Press 4
            ''')

        select=int(input("Proceed:"))

        if(select==1):
            a=int(input("Enter Id whose Name you want to Update:"))
            b=input("Enter Name:")
            t=(b,a)
            Update_Name(t)

        elif(select==2):
            a=int(input("Enter Id whose Department you want to Update:"))
            b=input("Enter Department:")
            t=(b,a)
            Update_Dept(t)

        elif(select==3):
            a=int(input("Enter Id whose Salary you want to Update:"))
            b=float(input("Enter Salary"))
            t=(b,a)
            Update_Sal(t)

        elif(select==4):
            a=int(input("Enter Id whose Details you want to Update:"))
            b=input("Enter Name:")
            c=input("Enter Department:")
            d=float(input("Enter Salary:"))
            t=(b,c,d,a)
            Update_Details(t)

        else:
            print("Invalid Response")

    elif(operation==3):
        print('''
            To Delete Name, Press 1
            To Delete Department, Press 2
            To Delete Salary, Press 3
            To Delete All Details, Press 4
            ''')

        option=int(input("Proceed:"))

        if(option==1):
            a=int(input("Enter Id Whose Name You want To Delete:"))
            Delete_Name(a)
            
        elif(option==2):
            a=int(input("Enter Id whose Department you want to Delete:"))
            Delete_Dept(a)

        elif(option==3):
            a=int(input("Enter Id whose Salary you want to Delete:"))
            Delete_Sal(a)

        elif(option==4):
            a=int(input("Enter Id whose Details you want to Delete:"))
            DeleteData(a)

        else:
            print("Invalid Response")

    elif(operation==4):
        print('''
            To View Name, Press 1
            To View Department, Press 2
            To View Salary, Press 3
            To View All Records, Press 4
            ''')

        step=int(input("Proceed:"))

        if(step==1):
            a=int(input("Enter Id whose Name you want to View:"))
            Show_Name(a)

        elif(step==2):
            a=int(input("Enter Id whose Department you want to View:"))
            Show_Dept(a)

        elif(step==3):
            a=int(input("Enter Id whose Salary you want to View:"))
            Show_Sal(a)

        elif(step==4):
            
            ShowDetails()

        else:
            print("Invalid Response")

    elif(operation==5):
        ext=input("Are You Sure, You Want To Exit? (Y/N):").lower()
        if(ext=='n'):
            continue
        else:
            print("Thank You")
            break
    else:
        print("Invalid Response.......Please Try Again")

















    












    
    
