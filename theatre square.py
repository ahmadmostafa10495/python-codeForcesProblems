
"""i=0
while 1:
    if n<=a:
        p=1
        break
    elif  (n+i)%a==0:
        p=(n+i)//a
        break
    i+=1
j=0    
while 1:
    if m<=a:
        o=1
        break
    elif  (m+j)%a==0:
        o=(m+j)//a
        break
    j+=1
print(p*o)        """
"""q=1
while 1:
    if n<=a:
        break
    elif (a*q)>=n:
        break
    q+=1

z=1
while 1:
    if m<=a:
        break
    elif (a*z)>=m:
        break
    z+=1
print (q*z)  """
n,m,k=map(int,input().split(' '))
w=(n+k-1)//k
h=(m+k-1)//k
print(w*h)

    
