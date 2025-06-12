import math as m
colunas=int(input())
valores=input().split()
valoresnum=[]
for i in valores:
    valoresnum.append(int(i))
linhas=max(valoresnum)

for i in range(linhas):
    final=""
    for j in valoresnum:
        diferenca=j-linhas
        if (diferenca)<0 and ((m.fabs(diferenca))>=i+1):
            final+="0 "
        elif (m.fabs(diferenca))<=i+1:
            final+="1 "
        else:
            final+="1 "
    print(final)