#TechSOC Task-2

import json

EE101="NA"
MA101="NA"
HS101="NA"     
EE102="NA"
MA102="NA"
HS102="NA"
EE103="NA"
MA103="NA"
HS103="NA"
EE104="NA"
MA104="NA"
HS104="NA"
EE105="NA"
MA105="NA"
HS105="NA"
EE106="NA"
MA106="NA"
HS106="NA"
BTP="NA"
Internship="NA"
EE108="NA"
EE109="NA"
EE110="NA"


def addkey(filepath,newkey,newvalue):
    with open(filepath,'r') as file:
        data=json.load(file)


    data[username]=password
    with open(filepath,'w') as file:
        json.dump(data,file,indent=4)
   
def SPI(sem):

    with open(filepathG,'r') as file:
        dataG=json.load(file)
    n=1
    sumSPI=0
    for sem in dataG[username]:
        
        semList=list(dataG[username][sem].values())
        semListM=[]
        total=0
        
        
        for i in semList:
            if i!="NA":
                ii=int(i)
                total=total+ii
                semListM.append(i)
        
        print("Semester "+str(n)+" SPI : \n"+str(total/len(semListM)))
        n=n+1
        sumSPI=sumSPI+(total/len(semListM))
    print("CPI="+str(sumSPI/8))
    

def loginS(username):
        

        with open(filepath,'r') as file:
            data=json.load(file)

        
        if username in data:

            m=0
            n=True
            while m<3 and n:

                password=input("Enter your password: ")
                
                if data[username]==password:
                    print("Login Succesful\n")

                    with open(filepathG,'r') as file:
                        dataG=json.load(file)
                    print(username+" Dashboard\n")

                    i=1
                    
                    for sem in dataG[username]:
                        ii=str(i)
                        print("Semester "+ii+" : ")
                        print(dataG[username][sem])
                        
                        i=i+1
                    

                    print(SPI(dataG[username]))
                    n=False
                    break
                
                    
       
                else:
                    print("Wrong Password. Please enter correct password.(Total only 3 tries)")
                    m=m+1
        else:
            print("This username does not exist, please enter correct username or try SignUp to create new username.")

def loginA(username):

        with open(filepathA,'r') as file:
            dataA=json.load(file)

        if username in dataA:
            
            x=0
            y = True
            while x<3 and y:

                password=input("Enter your password: ")
                
                if dataA[username]==password:
                    print("Login Succesful")

                    abc=False
                    while not abc:
                        studentusername=input("You want to manage which student's grade? \n Enter Student Username: ")
                        with open(filepath,'r') as file:
                            data=json.load(file)
                        
                            if studentusername in data:
                                abc=True
                                while True:
                                        
                                    semg=input("Enter the course semester: (1-8)")
                                    askg=input("Available Courses(4 credit each):\n Semester 1: MA101/EE101/HS101 \n Semester 2: MA102/EE102/HAS102 \n Semester 3: MA103/EE103/HS103 \n Semester 4: MA104/EE104/HS104 \n Semester 5: MA105/EE105/HS105 \n Semester 6: MA106/EE106/HS106 \n Semester 7: BTP/Internship \n Semester 8: EE108 \n For which course do you want to manage grades?")
                                    semgg="sem"+str(semg)

                                    with open(filepathG,'r') as file:
                                        dataG=json.load(file)                                
                                    
                                    if askg in dataG[studentusername][semgg]:
                                        enterG=input("Enter grade(on scale 1-10): ")

                                        with open(filepathG,'r') as file:
                                            dataG=json.load(file)
                                        valid=["NA","1","2","3","4","5","6","7","8","9","10"]
                                        if str(enterG) in valid:
                                            dataG[studentusername][semgg][askg]=enterG
                                            
                                            with open(filepathG,'w') as file:
                                                json.dump(dataG,file,indent=4)
                                            askc=input("Grades updated succesfully, \n if you want to exit press 'e'\n if you want to see student updated dashboard press 's' \n if you want to continue managing grades press anything except 'e','s' : ")
                                            if askc=="e":
                                                y=False
                                                break
                                            if askc=="s":
                                                with open(filepathG,'r') as file:
                                                    dataG=json.load(file)
                                                print(studentusername+" Dashboard")
                                                i=1
                            
                                                for sem in dataG[studentusername]:
                                                    ii=str(i)
                                                    print("Semester "+ii+" : ")
                                                    print(dataG[studentusername][sem])
                                
                                                    i=i+1
                                                y=False
                                                break
                                        else:
                                            print("enter valid input: (either 1-10 or NA)\nRepeat the process.")

                                            askc=input("If you want to exit press 'e'\n if you want to see student updated dashboard press 's' \n if you want to continue managing grades press anything except 'e','s' : ")
                                            if askc=="e":
                                                y=False
                                                break
                                            if askc=="s":
                                                with open(filepathG,'r') as file:
                                                    dataG=json.load(file)
                                                print(studentusername+" Dashboard")
                                                i=1
                            
                                                for sem in dataG[username]:
                                                    ii=str(i)
                                                    print("Semester "+ii+" : ")
                                                    print(dataG[studentusername][sem])
                                
                                                    i=i+1
                                                y=False
                                                break
                                    else:
                                        print("Enter valid course code.")
                            else:
                                print("Enter valid student username.")
                                
                else:
                    
                    print("Wrong Password. Please enter correct password.(Total only 3 tries)")
                    x=x+1

        else:
            print("This username does not exist, please enter correct username or try SignUp to create new username.")

    
filepath="c:\\Users\\ADMIN\\Desktop\\Python\\data.json"
filepathA="c:\\Users\\ADMIN\\Desktop\\Python\\dataA.json"
filepathG="c:\\Users\\ADMIN\\Desktop\\Python\\dataG.json"

signup=input("You have to Signup or Login? \n Press S for Signup and L for Login.")

if signup=="S":

    print("Are you a student or an admin?")
    ask1=input("If student enter S, if admin enter A")

    

    if ask1=="S":
        with open(filepath,'r') as file:
            data=json.load(file)
        username=input("Enter your username: (Format: 'Name Surname')")
        if username in data:
            print("Username already exits, try Login")
        else:
            password=input("Enter your password: ")
            addkey(filepath,username,password)
            
            with open(filepathG,'r') as file:
                dataG=json.load(file)
            dataG[username]={"sem1":{"EE101":EE101,
                                    "MA101":MA101,
                                    "HS101":HS101

                                  
                                    },
                             "sem2":{"EE102":EE102,
                                      "MA102":MA102,
                                      "HS102":HS102
                                  
                                 },
                            "sem3":{"EE103":EE103,
                                      "MA103":MA103,
                                      "HS103":HS103
                                  
                                 },
                            "sem4":{"EE104":EE104,
                                      "MA104":MA104,
                                      "HS104":HS104
                                  
                                 },
                            "sem5":{"EE105":EE105,
                                      "MA105":MA105,
                                      "HS105":HS105
                                  
                                 },
                            "sem6":{"EE106":EE106,
                                      "MA106":MA106,
                                      "HS106":HS106
                                  
                                 },
                            "sem7":{"BTP":BTP,
                                    "Internship":Internship
                                    
                                  
                                 },
                            "sem8":{"EE108":EE108,
                                      
                                  
                                 }
                           

                      }
            
            with open(filepathG,'w') as file:
                json.dump(dataG,file,indent=4)

            print("You can proceed for login: ")
            username=input("Enter your username: (Format: 'Name Surname')")
            loginS(username)

    if ask1=="A":
        with open(filepathA,'r') as file:
            data=json.load(file)
        username=input("Enter your username: (Format: 'Name Surname')")
        if username in data:
            print("Username already exits, try Login")
        else:
            password=input("Enter your password: ")
            addkey(filepathA,username,password)

            print("You can proceed for login: ")
            
            with open(filepathA,'r') as file:
                dataA=json.load(file)

            username=input("Enter your username: (Format: 'Name Surname')")
            loginA(username)
            
    else:
        print("Enter valid input. Either 'A' or 'S' in capital")
        
if signup=="L":
    print("Are you a student or an admin?")
    ask1=input("If student enter S, if admin enter A")

    
    

    if ask1=="S":

        with open(filepath,'r') as file:
            data=json.load(file)

        username=input("Enter your username: (Format: 'Name Surname')")
        loginS(username)
    
    if ask1=="A":

        with open(filepathA,'r') as file:
            dataA=json.load(file)

    
    
        username=input("Enter your username: (Format: 'Name Surname')")
        loginA(username)
        
    else:
        print("Enter valid input.Either 'A' or 'S' in capital")
        
else:
    print("Enter valid input. Either 'S' or 'L' in capital.")

        

    
        






