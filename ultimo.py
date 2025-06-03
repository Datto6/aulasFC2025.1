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