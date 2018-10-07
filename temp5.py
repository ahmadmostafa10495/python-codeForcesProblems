import math
def isprime (n):
    i=2
    while 1:
        if n%i==0:
            return False 
        
        if i>=math.sqrt(n):
            return True
        i+=1
x=int (input())
e=isprime(x)
if e==False:
    print ("not prime")

else:
    print("prime")





"""u=2
for f in range(2,int(math.sqrt(x))):
    if x%f==0:
        print ("not prime")
        break
    if u>=math.sqrt(x):
        print("prime")
        break
    u+=1"""
