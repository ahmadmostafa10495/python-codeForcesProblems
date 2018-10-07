def my_max (x,*y):
    maxi=x
    for i in y:
        if i>maxi:
            maxi=i
    return maxi
print(my_max(10,20))
print(my_max(10,20,30))
print(my_max(10,20,30,40))
