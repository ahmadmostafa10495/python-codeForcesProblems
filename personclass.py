class Person():
    ID=0
    def __init__ (self,name,address,contact_number,gender,age):
        self.name=name
        self.address=address
        self.contact_number=contact_number
        self.gender=gender
        self.age=age
        self.tempid=Person.ID
        Person.ID+=1

    def setname (self,name):
        self.name=name

    def getname (self):
        return self.name

    def setaddress (self,address):
        self.address=address

    def getaddress (self):
        return self.address

    def setcontact_number (self,contact_number):
        self.contact_number=contact_number

    def getcontact_number (self):
        return self.contact_number

    def setgender (self,gender):
        self.gender=gender

    def getgender (self):
        return self.gender

    def setage (self,age):
        self.age=age

    def getage (self):
        return self.age    
def createperson():
    tempname=input("please enter the person's name:")
    tempaddress=input("please enter the person's address:")
    tempcontact_number=input("please enter the person's contact number:")
    tempgender=input("please enter the person's gender:")
    tempage=input("please enter the person's age:")
    person.append(Person(tempname,tempaddress,tempcontact_number,tempgender,tempage))
person=[]
wannaout='y'
whatdoyouwant=""
while wannaout=='y':
    whatdoyouwant=input("what do you want sir/madame:")
    if whatdoyouwant=='create person':
        createperson()
    elif whatdoyouwant=='print person':
        whatid=int(input("please enter person's id:"))
        print("person's name:",person[whatid].getname(),"\n""person's address:",person[whatid].getaddress())
        print("person's contact number:",person[whatid].getcontact_number())
        print("person's gender:",person[whatid].getgender(),"\n""person's age:",person[whatid].getage())
    wannaout=input("if you want to continue press y:")






























    
    
    
