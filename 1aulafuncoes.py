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
