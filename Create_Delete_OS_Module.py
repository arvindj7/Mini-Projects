while(True):
    
    print("\nwelcome to my computer.......!".title())
    print("\nHelp Center:")
    print("1: list directory".title())
    print("2: create directory".title())
    print("3: show current directory".title())
    print("4: delete folder".title())
    print("5: delete file".title())
    print("6: create file".title())
    print("7: Exit\n")
        
    import os
    
    select=int(input("Select Operation: "))
    
    if(select==1):
            
        listdir=os.listdir()
        for data in listdir:
            print(data)

    elif(select==2):
            
        newfolder=input("Folder Name: ").strip().lower()
        makedir=os.mkdir(newfolder)

    elif(select==4):
            
        delfolder=input("Enter Folder name to delete:".title()).strip().lower()
        removefile=os.rmdir(delfolder)

    elif(select==5):
            
        delfile=input("enter file name to delete with extension:".title()).strip().lower()
        removefile=os.remove(delfile)

    elif(select==3):
            
        currentdir=os.getcwd()
        print("Current Directory---->",currentdir)

    elif(select==6):
        
        Name=input("enter name of file with extension: ".title())
        file=open(f"{Name}","w")
        content=input("Enter Content Of File: \n")
        file.write(content)
        print(f"File '{Name}' Created Successfully......!")
        file.close()
            
    elif(select==7):
        
        ext=input("are you sure, you want to exit? (Y/N): ".title()).strip().upper()
        if(ext=="Y"):
            break
        elif(ext=="N"):
            continue
        else:
            print("Invalid Response")
            print("Please Select Valid Response")
            
    else:
        print("Invalid Operation selected")
        
        
        
        


