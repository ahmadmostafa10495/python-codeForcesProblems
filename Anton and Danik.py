x=int(input())
y=input()
i=0
A=0
D=0
while i<len(y):
    if y[i]=='A':
        A+=1
    elif y[i]=='D':
        D+=1
    i+=1
if A>D:
    print("Anton")
elif D>A:
    print("Danik")
else:
    print("Friendship")
