n,k=map(int,input().split(' '))
"""i=1
j=1
r=((n+1)//2)+1
s=2
#while 1:
if k<= (n+1)//2:
        while 1:
            c=i
            if j==k:
                print(c)
                break
            i+=2
            j+=1
       # break            
elif k<=n:
        while 1:
            c=s
            if r==k:
                print (c)
                break
            s+=2
            r+=1
    #    break            
   # else:        
      #  k-=n"""
if k<= (n+1)//2:
    print(k*2 -1)
elif k<=n:
    k-=((n+1)//2)
    print(k*2)
