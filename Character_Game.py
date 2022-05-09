class Character():
    def __init__(self,name):
        self.name=name
                
        self.__life=3
        self.__score=0

    def kicked(self):
        self.__score+=10
                
    def punched(self):
        self.__score+=5
                
    def stabbed(self):
        self.__life-=1
                

    def displaylife(self):
        return self.__life

    def displayscore(self):
        return self.__score

    def intro(self):
        print(f"Name : {self.name}\nLife : {self.__life}\nScore : {self.__score}")

    

start="Mario Game"
print(start.center(20))
Name=input("Enter Your Name: ").title()
print(f"Hello {Name}.....Welcome To Mario World\n")
mario=Character(Name)
mario.intro()
    

print("k : kick")
print("p : punch")
print("s : Stabbed")
print("e : Exit\n")
while(True):
    
    
    c=input("Play Your Move: ")
        
    if(c=="k"):
        mario.kicked()
        print("Scored 10 Points")
        print("New Score: ",mario.displayscore())
        
    elif(c=="p"):
        mario.punched()
        print("Scored 5 Points")
        print("New Score: ",mario.displayscore())
        
    elif(c=="s"):
        lifecount=mario.displaylife()
        mario.stabbed()
        print("Got Stabbed.....Lost 1 Life")
        print("No. of Chances left: ",mario.displaylife())
        
        if(lifecount>1):
            continue
        else:
            print("Game Over")
            break
    elif(c=="e"):
        d=input("Are You Sure,(Y/N): ").lower()
        if(d=="y"):
            break
        elif(d=="n"):
            continue
        else:
            print("Invalid")
        



   
