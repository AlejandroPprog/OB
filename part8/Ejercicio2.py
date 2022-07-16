import pickle
class Vehiculo():
    color = ''
    motor = ''
    precio = 0.0

    def __init__(self, color, motor, precio):
        self.color = color
        self.motor = motor
        self.precio = precio

    def SoyCochazo(self):
        if self.precio > 40000:
            return 'Soy tremebundo coche'
        else:
            return 'Soy coche pocho'

SuperCoche = Vehiculo('negro', 'V8', 50000)
file = open('datos.bin', 'wb')
pickle.dump(SuperCoche, file)
file.close()
f = open('datos.bin', 'rb')
ArtoCoche = pickle.load(f)
print(ArtoCoche.motor)