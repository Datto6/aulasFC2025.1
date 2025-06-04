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
