import math 
x=int(input())
i=2
while 1:
    if x%i==0:
        
        break
    
    if i>=math.sqrt(x):
        print ("1",x)
        break
    i+=1
q=2
print("1",end=" ")
while 1:
   
    if x%q==0:
        print (q,end=" ")
    if q==x:
        break    
        
    q+=1
