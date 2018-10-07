x=input()
i=0
x= x.lower()
x= x.replace('e' ,"")
x= x.replace('i' ,"")
x= x.replace('o' ,"")
x= x.replace('y' ,"")
x= x.replace('a' ,"")
x= x.replace('u' ,"")
i=2
x="."+x
while i<len(x):
    x=x[:i]+"."+x[i:len(x)]
    i+=2
print (x)    
