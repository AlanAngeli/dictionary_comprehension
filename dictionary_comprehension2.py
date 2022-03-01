lista = [
    ("chave","valor"),
    ("chave2","valor2")
]

d1 = {x : y.upper() for x,y in lista}
d2 = {x.upper() : y for x,y in lista}
d3 = {x.upper() : y.upper() for x,y in lista}
print(lista)
print(d1)
print(d2)
print(d3)
print()