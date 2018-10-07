x=input()
y=input()
i=0
j=0
length=0
temp=0
"""while i<len(y):
    if y[i] not in x:
        temp+=1
    else:
        if temp>length:
            length=temp
        temp=0
    i+=1
    if i==len(y):
        if temp>length:
            length=temp
            
i=0
temp=0
while i<len(x):
    if x[i] not in y:
        temp+=1
    else:
        if temp>length:
            length=temp
        temp=0
    i+=1    
    if i==len(x):
        if temp>length:
            length=temp
            
print(length)


"""












while i<len(y):
    while j<len(x):
        if y[i]!=x[j]:
            temp+=1
        else:
            if temp>length:
                length=temp
            temp=0
        j+=1
        if j==len(x):
            if temp>length:
                length=temp
    temp=0    
    i+=1

i=0
j=0
temp=0

while i<len(x):
    while j<len(y):
        if x[i]!=y[j]:
            temp+=1
        else:
            if temp>length:
                length=temp
            temp=0
        j+=1
        if j==len(y):
            if temp>length:
                length=temp
    temp=0    
    i+=1
if length==0:
    length=-1
print(length)
    
