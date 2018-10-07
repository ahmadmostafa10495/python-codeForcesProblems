n,k=map(int,input().split(" "))
b=240-k
x=5
i=0
while x<=b and i<n:
    i+=1
    x+=(5*(i+1))
    
print(i)
