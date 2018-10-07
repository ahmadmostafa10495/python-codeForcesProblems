a=int(input())
b=int(input())
c=int(input())
m=(a+b)*c
t=a*(b+c)
if m<t:
    m=t
t=(a*b)+c
if m<t:
    m=t
t=a+(b*c)
if m<t:
    m+t
t=a+b+c
if m<t:
    m=t
t=a*b*c
if m<t:
    m=t
print (m)
