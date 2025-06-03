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