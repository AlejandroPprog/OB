numeroinicial = int(input('Entre su numero inicial: '))
numerofinal = int(input('Entre un numero final: '))
list = range(numeroinicial, numerofinal)
lista_de_numeros = []
i = numeroinicial
for i in list:
    if i%2 != 0:
        lista_de_numeros.append(i)
print(lista_de_numeros)
