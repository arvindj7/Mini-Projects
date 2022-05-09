#insert delete update

def createfile(ids,name,age,place,salary):
    #create
    
    file=open("login.txt","w")
    data=[]
    record=[ids,name,age,place,salary]
    data.append(record)
    print(data)

    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        print(i,n,a,p,s)
    file.close()
     

def addrecord(ids,name,age,place,salary):
    #insert
        
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    newrecord=[ids,name,age,place,salary]
    data.append(newrecord)

    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        #print(i,n,a,p,s)
    file.close()


def delrecord():
    #delete
        
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    ids=input("Enter Id:")
    name=input("Enter Name:")
    age=input("Enter Age:")
    place=input("Enter Place:")
    salary=input("Enter Salary:")

    record=[ids,name,age,place,salary]
    data.remove(record)

    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        print(i,n,a,p,s)
    file.close()


def ShowRec():
    #show
    file = open("login.txt","r")
    record = file.readlines()
    file.close()
    #print(record)

    for d in record:
        print(d)


def updaterec(ids,name,age,place,salary):
    #Update
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    print()
    newid=input("Enter New Id:")
    newname=input("Enter New Name:")
    newage=input("Enter New Age:")
    newplace=input("Enter New Place:")
    newsal=input("Enter New Salary:")

    
    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        #print(i,n,a,p,s)
    file.close()

    Delrecord(ids,name,age,place,salary)
    addrecord(newid,newname,newage,newplace,newsal)
    
    




def Delrecord(ids,name,age,place,salary):
    #delete
        
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    

    record=[str(ids),name,str(age),place,str(salary)]
    data.remove(record)

    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        #print(i,n,a,p,s)
    file.close()


while(True):
    print('''
        To Add Record,Press 1
        To Show Record,Press 2
        To Update Record,Press 3
        To Delete Record,Press 4
        ''')

    operation=int(input("Proceed: "))
    print()

    if(operation==1):
        ids=input("Enter Id: ")
        n_ame=input("Enter Name: ")
        a_ge=input("Enter Age: ")
        p_lace=input("Enter Place: ")
        s_alary=input("Enter Salary: ")
        addrecord(ids,n_ame,a_ge,p_lace,s_alary)
        print("Data Inserted Successfully......!")
        x=ShowRec()
        print(x)


    elif(operation==2):
        ShowRec()


    elif(operation==3):
        ShowRec()
        ids=input("Enter Id: ")
        n_ame=input("Enter Name: ")
        a_ge=input("Enter Age: ")
        p_lace=input("Enter Place: ")
        s_alary=input("Enter Salary: ")
        
        updaterec(ids,n_ame,a_ge,p_lace,s_alary)
        print("Data Updated Successfully......!")
        
        x=ShowRec()
        print(x)

    elif(operation==4):
        ShowRec()
        ids=input("Enter Id: ")
        n_ame=input("Enter Name: ")
        a_ge=input("Enter Age: ")
        p_lace=input("Enter Place: ")
        s_alary=input("Enter Salary: ")
        Delrecord(ids,n_ame,a_ge,p_lace,s_alary)
        print("Data Deleted Successfully.....!")
        ShowRec()
        
        





