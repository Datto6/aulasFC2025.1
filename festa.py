import math as m
import random
escola=int(input())
mercado=int(input())
loja=int(input())
distancias=[]
escola_merc=m.fabs(escola-mercado)
escola_loja=m.fabs(escola-loja)
loja_merc=m.fabs(mercado-loja)

if (escola>mercado and escola<loja) or (escola>loja and escola<mercado):
    dist_min=(escola_merc+escola_loja)*2
elif escola<mercado and escola<loja and mercado<loja:
    dist_min=(escola_merc+loja_merc)*2
elif escola<loja and escola<mercado and loja<mercado:
    dist_min=(escola_loja+loja_merc)*2
elif escola>mercado and escola>loja and mercado>loja:
    dist_min=(escola_merc+loja_merc)*2
elif escola>loja and escola>mercado and loja>mercado:
    dist_min=(escola_loja+loja_merc)*2
print(round(dist_min))