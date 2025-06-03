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