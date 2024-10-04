lista = [5, 6, 3, 9, 2, 12, 3, 8, 7]
# sorted(lista)

# metodo 1
# for i in lista:

# if i >= lista[-1]:
# lista.remove(i)
# lista.append(i)
# print(lista)

# metodo 2
print(len(lista))

for i in range(len(lista)):
    if lista[i] == 12:
        lista[i], lista[-1] = lista[-1], lista[i]

print(lista)
