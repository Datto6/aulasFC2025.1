limite=int(input())
partidas={}
def string_pnum(lista):
    retorno=[0]*(len(lista))
    for i in range(len(lista)):
        retorno[i]=int(lista[i])
    return retorno

for i in range(limite):
    partidas[i]=string_pnum(input().split())

for i in range(limite):
    total=0
    rodadas=0
    maximo=partidas[i][0]
    minimo=partidas[i][1]
    escolha_max=partidas[i][2]
    escolha=minimo
    while total<maximo:
        rodadas+=1
        total+=escolha
        escolha+=1
        if escolha>escolha_max:
            break
    print(rodadas)
