x=input()
i=0
l=0
u=0
while i<len(x):
    if x[i].islower():
        l+=1
    elif x[i].isupper():
        u+=1
    i+=1
if u>l:
    print(x.upper())
else:
    print(x.lower())
        
