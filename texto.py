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