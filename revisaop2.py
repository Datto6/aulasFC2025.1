import random as r
def transpostar(matriz):
    saida=[]
    for j in range(len(matriz[0])):
        linha=[]
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
        saida.append(linha)
    return saida

def soma_pares(lista):
    soma=0
    for i in lista:
        if i%2==0:
            soma+=i
    return soma

def maior_por_linha(matriz):
    lista=[]
    for i in range(len(matriz)):
        lista.append(max(matriz[i]))
    return lista

def contar_ocorrencias(lista,numero):
    vezes=0
    for i in lista:
        if i==numero:
            vezes+=1
    return vezes

def intercalar_listas(lista1,lista2):
    nova=[]
    for i in range(len(lista1)):
        nova.append(lista1[i])
        nova.append(lista2[i])
    return nova

def reverter_lista(lista):
    nova=[]
    for i in range(-1,-len(lista)-1,-1):
        nova.append(lista[i])
    return nova

def decimal_p_binario(numero):
    resultado=""
    while numero>0:
        resultado+=str(numero%2)
        numero=numero//2
    return resultado[::-1]

def cont_inicial(string):
    palavras=string.split()
    saida={}
    iniciais=[]
    for i in palavras:
        if i[0] not in iniciais:
            saida[i[0]]=1
            iniciais.append(i[0])
        else:
            saida[i[0]]+=1

    return saida

def rotacionar(lista,n):
    for i in range(n):
        lista.insert(0,lista.pop())
    return lista

def busca_binaria(lista,valor):
    tentativas=0
    achou=False
    inicio=0
    fim=len(lista)-1
    while not achou and (inicio<=fim):
        tentativas+=1
        meio=(inicio+fim)//2
        if meio==valor:
            achou=True
            break
        elif meio>valor:
            fim=meio-1
        else:
            inicio=meio+1
    return tentativas

print(busca_binaria([4.5, 5.0, 5.5, 6.0, 7.5, 8.0, 8.5, 9.0, 10.0],5.0))

import random as r
import math as m
def primos(n):
    achados=0
    numero=2
    primos=[]
    while achados<n:
        primo=True
        for i in range(2,numero):
            if numero%i==0:
                primo=False
                break
        if primo:
            achados+=1
            primos.append(numero)
        numero+=1
    return primos

def primos(limite):
    numero=2
    primos=[2]
    while max(primos)<limite:
        primo=True
        for i in range(2,numero):
            if numero%i==0:
                primo=False
                break
        if primo:
            primos.append(numero)
        numero+=1
        print(numero)
    return primos

def repetidos(lista):
    nova=[]
    usados=[]
    for i in lista:
        if lista.count(i)>1 and i not in usados:
            nova.append(str(i)+"^"+str(lista.count(i)))
            usados.append(i)
        elif lista.count(i)==1 and i not in usados:
            nova.append(str(i))
            usados.append(i)
    return nova

def matriz():
    matriz=[]
    for i in range(3):
        linha=[]
        for j in range(3):
            linha.append(int(r.randint(0,10)))
        matriz.append(linha)
    return matriz

def det(matriz):
    for i in range(3):
        det=matriz[0][i]*(matriz[i+1][i+1]*matriz[i+2])
    termo1=matriz[0][0]*(matriz[1][1]*matriz[2][2]-matriz[1][2]*matriz[2][1])
    termo2=matriz[0][1]


def ordenar_select(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            minimo=min(lista[i+1:])
            indexo=lista.index(minimo)
            if lista[i]>minimo:
                lista[i],lista[indexo]=lista[indexo],lista[i]
    return lista

def ordenar_bubble(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista

def romanos(numero):
    saida=""
    saida+="M"*(numero//1000)
    novo=numero%1000
    saida+="D"*(novo//500)
    novo%=500
    saida+="C"*(novo//100)
    novo%=100
    saida+="L"*(novo//50)
    novo%=50
    saida+="X"*(novo//10)
    novo%=10
    saida+="V"*(novo//5)
    novo%=5
    saida+="I"*(novo//1)
    return saida

def fat_primos(numero):
    maximo=m.sqrt(numero)
    fatores=primos(maximo)
    saida=[]
    print(fatores)
    for i in fatores:
        resultado=1
        teste=i
        potencia=0
        if numero%i==0:
            while resultado<numero:
                resultado*=teste
                potencia+=1
            saida.append(str(i)+"^"+str(potencia))
    return saida
