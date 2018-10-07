x=[str(i)for i in input()]
y=[str (r) for r in input()]
i=0
while i<len(x):
    if y[i]!=x[len(x)-1-i]:
        print("NO")
        break
    i+=1
else:
    print("YES")
    """
        










if y==x.reverse():
    print("YES")
else:
    print ("NO")
print (y,x.reverse(),x)
"""
