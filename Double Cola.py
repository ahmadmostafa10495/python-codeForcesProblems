n=int(input())
if n<=5:
    n/=5
    if n<=0.2:
        print("Sheldon")
    elif n<=0.4:
        print ("Leonard")
    elif n<=0.6:
        print ("Penny")
    elif n<= 0.8:
        print ("Rajesh")
    else:
        print ("Howard")
else :       
    while n>5:
        n-=5
    n/=5    
    if n<=0.2:
        print("Sheldon")
    elif n<=0.4:
        print ("Leonard")
    elif n<=0.6:
        print ("Penny")
    elif n<= 0.8:
        print ("Rajesh")
    else:
        print ("Howard")    
    
