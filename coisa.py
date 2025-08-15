def string_pnum(lista):
    retorno=[0]*(len(lista))
    for i in range(len(lista)):
        retorno[i]=int(lista[i])
    return retorno

qntd_tipo=string_pnum(input().split())
tipos=string_pnum(input().split())
precos=string_pnum(input().split())
clientes=int(input())
decisos=string_pnum(input().split())
produtos={
    "Numero":[],
    "Tipo":[],
    "Preco":[]
}
total=0
for i in range(qntd_tipo[0]):
    produtos["Numero"].append(i)
    produtos["Tipo"].append(tipos[i])
    produtos["Preco"].append(precos[i])

for i in range(clientes):
    tipo=decisos[i]
    if tipo==0:
        indexocomprado=produtos["Preco"].index(min(produtos["Preco"]))
        comprado=produtos["Preco"][indexocomprado]
        produtos["Preco"].remove(produtos["Preco"][indexocomprado])
        print(indexocomprado)
        total+=comprado
        produtos["Numero"].remove(indexocomprado)
        produtos["Tipo"].remove(produtos["Tipo"][indexocomprado])
    else:
        indexos_do_tipo=[]
        for j in range(len(produtos["Tipo"])):
            if tipo==produtos["Tipo"][j]:
                indexos_do_tipo.append(j)
        escolha_compras=[]
        for j in range(len(indexos_do_tipo)):
            escolha_compras.append(produtos["Preco"][indexos_do_tipo[j]])
        escolhido=min(escolha_compras)
        total+=escolhido
        indexocomprado=produtos["Preco"].index(escolhido)
        print(indexocomprado)
        produtos["Numero"].remove(indexocomprado)
        produtos["Tipo"].remove(produtos["Tipo"][indexocomprado])
    print(produtos)
    print(total)

print(total)
        
