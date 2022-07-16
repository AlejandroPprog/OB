from xml.dom.minidom import Notation


class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
#esto es redundante pero igual lo coloco para agarrar practica
    def Nota(self):
        return self.nota
    def Nombre(self):
        return self.nombre
#Suponiendo que nota de aprobado es 5
    def ResultadoFinal(self):
        if self.nota >= 5:
            print('El alumno', self.Nombre(), 'ha aprobado el curso con', self.Nota())
        else:
            print('El alumno', self.Nombre(), 'NO ha aprobado el curso con', self.Nota())

Alumno1 = Alumno("Carlos Arguiñano", 2)
Alumno2 = Alumno("Trump", 4.9)
Alumno3 = Alumno("Karl", 10)
Alumno4 = Alumno("Marx", 6)
Alumno1.ResultadoFinal()
Alumno2.ResultadoFinal()
Alumno3.ResultadoFinal()
Alumno4.ResultadoFinal()