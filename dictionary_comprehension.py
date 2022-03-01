lista = [
    ("chave","valor"),
    ("chave2","valor2")
]

d1 = dict(lista)
print(lista)
print()
###terá o mesmo resultado que:

d2 = {x:y for x,y in lista} #porém, aqui podemos fazer mais coisas, como multiplicar....
print(d2)
print()

##ex:

d3 = {x : y * 2 for x,y in lista}
d4 = {x * 2 : y * 2 for x,y in lista}
d5 = {x * 2 : y for x,y in lista}
print(d3)
print(d4)
print(d5)
print()
##mais exemplos:

lista2 = [
    ("chave",2),
    ("chave2",5)
]

d6 = {x : y * 2 for x,y in lista2}
d7 = {x * 2 : y * 2 for x,y in lista2}
d8 = {x * 2 : y for x,y in lista2}
print(lista2)
print(d6)
print(d7)
print(d8)
print()
