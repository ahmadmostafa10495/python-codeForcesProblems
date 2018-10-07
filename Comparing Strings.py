x=input()
y=input()
y=y[1]+y[0]+y[2:len(y)]
if x==y:
    print("YES")
else:
    print("NO")
