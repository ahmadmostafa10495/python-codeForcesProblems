x=int(input())
v=[int(c) for c in input().split()]
v.sort()

while x>0:
    x-=1
    print (v[x],end=(" "))
