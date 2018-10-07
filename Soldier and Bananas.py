k,w,n=map(int,input().split(' '))
money=0
while n>0:
    money=money+(k*n)
    n-=1
if money>w:
    print(money-w)
else:
    print ("0")
