NoOfAtt=int(input())
NoOfM,NoOfL=map(int,input().split(" "))
CounterForCardsM=0
Marcos=[]
CounterForCardsL=0
Leo=[]
while CounterForCardsM<NoOfM:
        a = [int(NoOfAtt) for NoOfAtt in input().split()]
        Marcos.append(a)
        CounterForCardsM+=1

while CounterForCardsL<NoOfM:
        b = [int(NoOfAtt) for NoOfAtt in input().split()]
        Leo.append(b)
        CounterForCardsL+=1
M,L=map(int,input().split(" "))
M-=1
L-=1
Att=int(input())
Att-=1
if Marcos[M][Att]>Leo[L][Att]:
    print("Marcos")
elif     Marcos[M][Att]<Leo[L][Att]:
    print ("Leonardo")
elif     Marcos[M][Att]==Leo[L][Att]:
    print("Empate")
