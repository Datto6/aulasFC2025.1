# dic={}
# while True:
#     key=input("Fala o indice. Aperta f se quiser parar")
#     if key=="f":
#         break
#     dic[key]=int(input("Fala o valor q c quer pro indice q vc acabou de botar")) ---> cria com so valores maiores que 10
# dic2={}
# for key,value in dic.items():
#     if value>10:
#         dic2[key]=value

# print(dic)
# print(dic2)
nomes=[]
while True:
    nome=input("Da um nome. Aperta f se for parar")
    if nome=="f":
        break
    else:
        nomes.append(nome)
dic={}
for i in nomes:
    primeira=i[0].upper()
    if dic.get(primeira) not in dic.values():
        dic[primeira]=[i]
    else:
        dic[primeira].append(i)

print(nomes)
print(dic)
