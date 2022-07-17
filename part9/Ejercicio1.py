#Porbando: lista = 'España, Argentina, EE.UU, Alemania, Japon, China, España, Brasil, Alemania, Brasil'
lista = input('Ingrese los paises separados por coma: ')
lista = lista.replace(',', '')
lista = lista.split()
lista = set(lista)
print('La lisa de paises es:', sorted(lista))
