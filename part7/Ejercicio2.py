import time
hora = time.ctime()
minutos = hora[14] + hora[15]
hora = hora[11] + hora[12]
hora = int(hora)
minutos = int(minutos)
print('Ahora son las {}:{}'.format(hora, minutos))
if hora < 19:
    restante = 19 - hora
    restantemin = 60 - minutos
    print('Te faltan {}:{} hora mas para irte del trabajo'.format(restante, restantemin))
else:
    print('Te puedes ir a casa')