x=input()
y=input()
r=[]
i=0
p=""
while i<len(x):
    if x[i]==y[i]:
        r+=x[i]
        
    elif ord(x[i])==ord(y[i])+1 or ord(x[i])==ord(y[i])-1:
        print("No such string")
        break
    else:
        if ord(x[i])>ord(y[i]):
            c=ord(y[i])+1
            r+=chr(c)
            i+=1
            while i<len(x):
                r+='a'
                i+=1
            m=0    
            while  m< len(x):
                p+=r[m]
                m+=1
            print(p)    
            break
        if ord(y[i])>ord(x[i]):
            c=ord(x[i])+1
            r+=chr(c)
            i+=1
            while i<len(x):
                r+='a'
                i+=1
            m=0    
            while  m< len(x):
                p+=r[m]
                m+=1
            print(p)    
            break
    i+=1
    
        
