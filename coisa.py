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

print(dic)
print(dic2)
print(dic3)