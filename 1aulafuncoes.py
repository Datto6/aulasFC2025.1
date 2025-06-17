# coisa=input("Da um string ai")
# def maiuscula(string):
#     print(string.upper())
# try:
#     maiuscula(234)
# except:
#     print("Teu negocio  deu ruim")

numeros=input("DA um ngc de numeros sem espaco ae, se tiver letra ou outro da erro")
def soma(numeros):
        lista=[]
        for i in numeros:
            lista.append(int(i))
        return sum(lista)
try :
    print(soma(numeros))
except:
    print("Deu ruim cr")

def criamatriz():
    matriz=[]
    linhas=int(input("Quantas linhas tu quer"))
    colunas=int(input("Quantas colunas"))
    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(input("Fale valor para linha"+str(i)+" Coluna"+str(j)))
        matriz.append(linha)
    return matriz

def soma_colunas(matriz):
    soma=[]
    for j in range(len(matriz[0])):
        contador=0
        for i in range(len(matriz)):
            contador+=int(matriz[i][j])
        soma.append(contador)
    return soma

def palindromao(frases):
    saida=[]
    for i in frases:
        stringuin=i.split()
        for i in stringuin:
            ajustado=i.lower()
            if ajustado[::-1]==ajustado and ajustado.isalpha():
                saida.append(i)

    return saida
def listastring():
    saida=[]
    numstring=int(input("Quantos strings vc quer"))
    for i in range(numstring):
        saida.append(input("Da 1 ai"))
    return saida


def rotacionar(lista,numero):
    for i in range(numero):
        lista.insert(0,lista.pop())
    return lista

print(rotacionar([1,2,3,4],3))
