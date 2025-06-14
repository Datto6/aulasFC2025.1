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
