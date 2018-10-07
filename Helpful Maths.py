x=input()
x=x.replace('+','')
t=[str(i) for i in x]
t.sort()
o=""
q=0
while q<len(t):
    o+=t[q]
    q+=1
q=1
while q<len(o):
    o=o[:q]+'+'+o[q:len(o)]
    q+=2
print(o)
