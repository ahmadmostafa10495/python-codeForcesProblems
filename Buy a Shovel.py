k,r=map(int,input().split(" "))
i=0
while 1:
    if k<10 and k==r:
            print ("1")
            break
    elif k%10==0:
        print ("1")
        break
    i+=1
    if ((k*i)-r)%10==0:
        print(i)
        break
    elif    ((k*i))%10==0:
        print (i)
        break
            
