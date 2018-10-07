n,m=map(int,input().split(" "))
if n%2==0:
    i=n//2
else:
    i= (n+1)//2
while i<=n:
    if i%m==0:
        print (i)
        break
    i+=1
else :
    print ("-1")
