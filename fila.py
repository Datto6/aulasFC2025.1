numero=int(input())
alturas=input().split()
alturasnum=[]
for i in alturas:
    alturasnum.append(int(i))
maisalto=0
vistos=0
for i in range(-1,-len(alturasnum)-1,-1):
    if alturasnum[i]>maisalto:
        maisalto=alturasnum[i]
        vistos+=1
print(numero-vistos)