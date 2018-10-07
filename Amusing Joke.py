x=[str(i1) for i1 in input()]
y=[str(i2) for i2 in input()]
z=[str(i3) for i3 in input()]
t=x+y
t.sort()
z.sort()
if z==t:
    print ("YES")
else:
    print("NO")
   
