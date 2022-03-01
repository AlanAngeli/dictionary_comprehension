d1 = {x: y for x, y in enumerate(range(5))}
print(d1)
print()

d2 = {x for x in range(5)}
print(d2)
print()

d3 = {f'chave_{x}': x**2 for x in range(5)} ##adiciona a string 'chave', fa
print(d3)
print()
