estoque={}
while True:
    key=input("Fala o produto. Aperta f se quiser parar")
    if key=="f":
        break
    estoque[key]=int(input("Fala quantos tem"))

vendas={}
print("Agora p vendas ")
for key in estoque.keys():
    vendas[key]=int(input("Fala quantos vc vendeu do produto "+str(key)))

saida={}

for key,value in estoque.items():
    saida[key]=estoque[key]-vendas[key]

print(estoque)
print(vendas)
print(saida)

dic={}
while True:
    key=input("Fala o produto. Aperta f se quiser parar")
    if key=="f":
        break
    dic[key]=int(input("Fala qnts tem"))

dic2={}
print("Agora pro estoque 2")
while True:
    key=input("Fala o indice. Aperta f se quiser parar")
    if key=="f":
        break
    dic2[key]=int(input("Fala qnts tem"))

dic3={}
for key in dic.keys():
    if key in dic2.keys():
        dic3[key]=dic[key]+dic2[key]

print(dic)
print(dic2)
print(dic3)

# texto=input("Da tua frase ae")
# minusculo=texto.lower()
# lista=minusculo.split()
# nova=[]
# for i in lista:
#     if len(i)>=4:
#         nova.append(i)

# dic={}
# for i in nova:
#     if dic.get(i) not in dic.values(): --> conta palavras 
#         dic[i]=1
#     else:
#         dic[i]+=1

# print(nova)
# print(dic)

dic={}
while True:
    key=input("Fala o produto. Aperta f se quiser parar")
    if key=="f":
        break
    notas=[]
    while True:
        nota=int(input("Da a nota do aluno q tu falou, aperta -1 p parar"))
        if nota==-1:
            dic[key]=notas
            break
        else:
            notas.append(nota)
dic2={}
for key,value in dic.items():
    soma=sum(value)
    media=round(soma/len(value))
    dic2[key]=media

print(dic)
print(dic2)

# palavra=input("Da uma palavra ae") --> conta chars na palavra
# dic={}
# for i in palavra:
#     cont=0
#     for j in palavra:
#         if j==i:
#             cont+=1

#     dic[i]=cont

# print(dic)

dic={}
while True:
    key=input("Fala o indice. Aperta f se quiser parar")
    if key=="f":
        break
    dic[key]=input("Fala o valor q c quer pro indice q vc acabou de botar")

dic2={}
for key,value in dic.items():
    dic2[value]=key

print(dic)
print(dic2)

dic={}
while True:
    key=input("Fala o indice. Aperta f se quiser parar")
    if key=="f":
        break
    dic[key]=int(input("Fala o valor q c quer pro indice q vc acabou de botar"))

dic2={}
print("Agora p segunda dic")
for key in dic.keys():
    dic2[key]=int(input("Fala o numero pro indice "+str(key)))

dic3={}
for key,value in dic.items():
    dic3[key]=dic[key]+dic2[key]


# vetor=[1,2,3]
# matriz=[[3,4,66],[32,3,-3],[-23,-42,32],[2,2,2]]
# linhas=len(matriz)
# colunas=len(matriz[0])
# j=0
# vet2=[]
# for i in range(linhas):
#     somatorio=0
#     for j in range(colunas):
#         elemento=matriz[i][j]
#         novo=elemento*vetor[j] ----> Isso multiplica vetor por matriz
#         somatorio+=novo
#     vet2.append(somatorio)

# print(vet2)

# Em baixo tentarei matrix x matriz

vetor=[[1,2,3,7,8],
       [32,-34,53,45,-89],
       [13,0,54,2,0]
       ]

matriz=[[3,4,66],
        [32,3,-3],
        [-23,-42,32],
        [2,2,2],
        [4,5,7]
        ]

linhas=len(vetor)
colunas=len(vetor[0])

vet2=[]
for i in range(linhas):
    linhanova=[]
    somatorio=0
    for j in range(len(matriz[0])):
        for k in range(len(matriz)):
            elemento=vetor[i][k]
            novo=elemento*matriz[k][j]
            somatorio+=novo
        linhanova.append(somatorio)
        somatorio=0
    vet2.append(linhanova)

print(vet2)
