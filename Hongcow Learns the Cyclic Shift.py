x=input()
y=x

i=0

a=[]
a.append(y)
while i<len(x):
    y=y[len(x)-1]+y[0:len(x)-1]
    
    a.append(y)
    i+=1
    
        
print(len(set(a)))
