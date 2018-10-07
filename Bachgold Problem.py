x=int(input())
if x%2==0:
    print(x//2)
    y=x//2
    print("2 "*y)
else:
    v=x-3
    n=v//2
    print(n+1)
    print("2 "*n+"3")
