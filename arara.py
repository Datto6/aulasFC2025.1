
def string_pnum(lista):
    retorno=[0]*(len(lista))
    for i in range(len(lista)):
        retorno[i]=int(lista[i])
    return retorno

arara_gaiola=string_pnum(input().split())
araras=arara_gaiola[0]
gaiolas=arara_gaiola[1]

for i in range(gaiolas):
    if i%5==0:
        araras-=1

if araras==0:
    print("S")
else:
    print("N")
    