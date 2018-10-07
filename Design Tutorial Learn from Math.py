x=int(input())
import math
def isprime (n):
    i=2
    while 1:
        if n%i==0:
            return False
        
        if i>=math.sqrt(n):
            return True
        i+=1
def test (a):
    """ if a==15:
        print ("6 9")
        return"""
    c=a
    e=0
    while 1:
        c-=4
        e+=1
        r= not isprime(a-(4*e))
        if  r:
            print (c,a-c)
            return
test(x)        
        
        
