"""def my_isalfa (x):
     for i in range( len(x)):
        ''' if x[i] !='0' and x[i]!='1' and x[i]!='2' and x[i]!='3' and x[i]!='4' and x[i]!='5' and x[i]!='6' and x[i]!='7' and x[i]!='8' and x[i]!='9' :'''
        if (x[i]>='z' and x[i]<='a' )and (x[i]>='Z' and x[i]<= 'A')== False:
             return False
     else :
         return True
x=input()
print (my_isalfa (x))"""



   
     
def my_isalfa (x):
     a = [str (e) for e in x]
     for i in range( len(x)):
         if (a[i]>'z' or a[i]<'a' )== False:
              c = ord(a[i])
              c -= 32
              a[i] = chr(c)
              
         elif   (a[i]>'Z' or a[i]< 'A')== False:
             b = ord(a[i])
             b += 32
             a[i] = chr(b)
       
     r=""        
     for i in range (len(a)):
        r+=a[i] 
     return r
         
x=input()
print (my_isalfa (x))
