from functools import reduce
listanum = range(50)
listaimpar = list(filter(lambda x: x % 2, listanum))
resultado = reduce(lambda x,y: x + y, listaimpar)
print(listaimpar)
print(resultado)