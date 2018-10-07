from random import *
def my_uni (x,y):
    return (random()*(y-x))+x
x,y=map (int,input().split(" "))
print(my_uni(x,y))
