def ponta(i,j,mat):
    if j+1==len(mat[i]) or j-1==-1 or i-1==-1 or i+1==len(mat):
        return True
    else:
        return False
def printarmatriz(matriz):
    for i in range(len(matriz)):
        linha=""
        for j in range(len(matriz[0])):
            linha+=str(matriz[i][j])+" "
        print(linha)

def string_pnum(lista):
    retorno=[0]*(len(lista))
    for i in range(len(lista)):
        retorno[i]=int(lista[i])
    return retorno

def direita(i,j,mat):
    if j+1==len(mat[i]):
        return True
    if (mat[i][j+1]+mat[i][j])%2!=0:
        return True
    else:
        return False

def esquerda(i,j,mat):
    if j-1==-1:
        return True
    if (mat[i][j-1]+mat[i][j])%2!=0:
        return True
    else:
        return False

def cima(i,j,mat):
    if i-1==-1:
        return True
    if (mat[i-1][j]+mat[i][j])%2!=0:
        return True
    else:
        return False

def baixo(i,j,mat):
    if i+1==len(mat):
        return True
    if (mat[i+1][j]+mat[i][j])%2!=0:
        return True
    else:
        return False
def soma(i,j,mat):
    s=0
    if not ponta:
        s+=mat[i+1][j]
        s+=mat[i-1][j]
        s+=mat[i][j+1]
        s+=mat[i][j-1]
    elif j+1==len(mat[i]):
        s+=mat[i+1][j]
        s+=mat[i-1][j]
        s+=mat[i][j-1]
    elif i-1==-1:
        s+=mat[i+1][j]
        s+=mat[i][j-1]
        s+=mat[i][j+1]
    elif j-1==-1:
        s+=mat[i+1][j]
        s+=mat[i-1][j]
        s+=mat[i][j+1]
    return s
    
linha_coluna=string_pnum(input().split())
matriz=[]

for i in range(linha_coluna[0]):
    matriz.append(string_pnum(input().split()))

nova=[]
ok=True
for i in range(len(matriz)):
    linhanova=[]
    for j in range(len(matriz[0])):
        if esquerda(i,j,matriz) and direita(i,j,matriz) and cima(i,j,matriz) and baixo(i,j,matriz):
            linhanova.append(0)
        else:
            linhanova.append(1)
            ok=False
    nova.append(linhanova)
printarmatriz(nova)
mudados=0
indexos=[]
if not ok:
    for i in range(len(nova)):
        for j in range(len(nova[0])):
            if not (esquerda(i,j,nova) and direita(i,j,nova) and cima(i,j,nova) and baixo(i,j,nova)):
                if soma(i,j,nova)==4:
                    mudados+=1
                    indexos.append((i,j))

for i in indexos:
    linha=i[0]
    coluna=i[1]
    matriz[linha][coluna]+=1

print(mudados)
printarmatriz(matriz)

