x=input()
i=0
e='a'
p=0
while i<len(x):
    d=abs(ord(x[i])-ord(e))
    if d>13:
        d=26-d
    p+=d    
    e=x[i]
    i+=1
print(p)
    
