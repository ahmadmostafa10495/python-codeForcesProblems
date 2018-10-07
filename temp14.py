class Robot :
    id1=0
    def print_robot_details(self):
        print("robot name:",self.name)
        print("robot color:",self.color)
        print("robot code:",self.code)
        print("robot length:",self.length)
        print("robot wieght:",self.wieght)
    def __init__(self,name,color,length,wieght):
        self.name=name
        self.color=color
        self.length=length
        self.wieght=wieght
        self.code=Robot.id1
        Robot.id1+=1
    def setname (self,name):
        self.name=name

    def getname (self):
        return self.name

    def setcolor (self,color):
        self.color=color

    def getcolor (self):
        return self.color    

    def getcode (self):
        return self.code

    def setlength (self,length):
        self.length=length

    def getlength (self):
        return self.length

    def setwieght (self,wieght):
        self.wieght=wieght

    def getwieght (self):
        return self.wieght  




class PlayerRobot (Robot):
    def __init__(self,name,color,length,wieght,position,number,time):
        '''self.name=name
        self.color=color
        self.length=length
        self.wieght=wieght
        self.code=Robot.id1
        Robot.id1+=1'''
        super(PlayerRobot,self).__init__(name,color,length,wieght)
        self.position=position
        self.number=number
        self.time=time
    def setposition (self,position):
        self.position=position

    def getposition (self):
        return self.position

    def setnumber (self,number):
        self.number=number

    def getnumber (self):
        return self.number

    def settime (self,time):
        self.time=time

    def gettime (self):
        return self.time  





x=PlayerRobot("x","red",11,11,"CMF",33,80)
y=PlayerRobot("y","green",11,11,"LM",44,70)
z=PlayerRobot("z","white",11,11,"CF",10,90)







x.setname("moteb")
x.setlength(184)
x.setcolor("blue")
x.setwieght(100)
x.setposition("CF")
x.setnumber(9)
x.settime(95)




print(x.getcode(),x.getcolor(),x.getlength(),x.getname(),x.getwieght(),x.getposition(),x.getnumber(),x.gettime())























"""x=Robot("x","red","11","11")
y=Robot("y","green","12","12")
z=Robot("z","white","13","13")
x.print_robot_details()
y.print_robot_details()
z.print_robot_details()
x.setname("robo1")
x.setlength(184)
x.setcolor("blue")
x.setwieght(150)
print(x.getcode(),x.getcolor(),x.getlength(),x.getname(),x.getwieght())"""













