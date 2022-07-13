import math
def areaTri( alt, base):
    return (alt*base)/2

def areaCir(radio):
    return math.pi*(radio**2)

altura = float(input('Ingrese una altura: '))
base = float(input('Ingrese la base: '))
radio = float(input('Ingrese el radio: '))
area = areaTri(altura, base)
areacirculo = areaCir(radio)
print('El area de su tiangulo es %.2f, y la de su circulo es %.2f' % (area, areacirculo))