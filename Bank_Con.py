class User():
    objcount=0
    no=1
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.Account_No=f"101{self.name}{User.no}"
        User.objcount+=1
        User.no+=1

    def showdetails(self):
        print(f"Name : {self.name}\nGender : {self.gender}")
        print(f"Account No :{self.Account_No}")
    
class Bank(User):
    __balance=0
    

    def __init__(self,name,gender):
        super().__init__(name,gender)

    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print(f"{amount} deposited in account".title())
        print("Current Balance :",self.__balance)

    def withdraw(self,amount):
        if(amount>self.__balance):
            print("Insufficient Balance")
            print("Current Balance :",self.__balance)
        elif(amount>=100 and amount<=self.__balance):
            self.__balance-=amount
            print(f"{amount} debited from account".title())
            print("Current Balance :",self.__balance)
            print("thank you for visiting".title())
            
        elif(amount<100):
            print("you cannot withdraw less than 100".title())
            return self.__balance

    def viewbalance(self):
        print(f"Account No :",self.Account_No)
        print("Current Balance :",self.__balance)

    def transfer(self,amount,User):
        if(amount>self.__balance):
            print("Insufficient Balance")
            return self.__balance
        elif(amount>=1 and amount<=self.__balance):    
            self.__balance=self.__balance-amount
            User.__balance=User.__balance+amount
            print(f"Successfully Transfered {amount} to {User.name}")
            print("Current Balance :",self.__balance)
        elif(amount<1):
            print("you cannot transfer less than 1".title())

        
print("Welcome To XYZee Bank")
#Taking Input for creating object
print()
name=input("Enter Your Name: ").strip().upper()
gender=input("Enter Your Gender: ").strip().lower()
#Creating Object
obj=Bank(name,gender)
users=['ARVIND','JENA']
print(f"Welcome.....{name}")

while(True):
    print('''
        1: Account Details
        2: Balance Enquiry
        3: Deposit Amount
        4: Withdraw Money
        5: Transfer Money
        6: Exit
        ''')

    operation=int(input("Proceed: "))
    print()

    if(operation==1):
        obj.showdetails()

    elif(operation==2):
        obj.viewbalance()

    elif(operation==3):
        depamount=int(input("Enter Amount You Want To Deposit: "))
        obj.deposit(depamount)

    elif(operation==4):
        withamount=int(input("Enter Amount You Want To Withdraw: "))
        obj.withdraw(withamount)

    elif(operation==5):
        name1=input("Enter Name Of User You Want To Transfer: ").strip().upper()
        gen1=input("Enter Gender: ")
        obj1=Bank(name1,gen1)
        tranamount=float(input("Enter Amount You Want To Tranfer: "))
        if(name1 in users):
            obj.transfer(tranamount,obj1)
            obj1.viewbalance()
        else:
            print("No Such User")

        
    elif(operation==6):
        print("Are you sure you want to exit?\n")
        ext=input("Enter your choice : ").upper()
                
        if (ext=='Y'):
            print("Thank you for visiting!!!")
            break
                
        
        elif(ext=='N'):
            continue
                
        else:
            print("Invalid Response!! please enter again\n")
    else:
        print("Invalid Response!! please enter again\n")

            

    
