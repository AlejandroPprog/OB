class Vehículo():
    color = None
    puertas = None
    ruedas = 4
    def color(self):
        return self._color
    def puertas(self):
        return self._puertas
    def ruedas(self):
        return self._puertas
    def setColor(self, color):
        self.color = color
    def setPuertas(self, puertas):
        self.puertas = puertas

class Coche(Vehículo):
    def __init__(self):
        self.Velocidad = 0
        self.Cilindrada = 0
    def Despacito(self):
        self.Velocidad = 20
        self.Cilindrada = 600
    def TodaMecha(self):
        self.Velocidad = 120
        self.Cilindrada = 1000

CocheMolongo = Coche()
CocheMolongo.setColor("Rojo")
CocheMolongo.setPuertas(4)
print("Quieto parao con el coche molongo", CocheMolongo.color, 'de', CocheMolongo.puertas, 'puertas')
CocheMolongo.Despacito()
print("Voy de", CocheMolongo.Velocidad)
CocheMolongo.TodaMecha()
print('A', CocheMolongo.Velocidad)