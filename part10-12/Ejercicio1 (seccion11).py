import sqlite3

tabla = sqlite3.connect('tabla.db')
cursor = tabla.cursor()

cursor.execute('''CREATE TABLE Alumnos(id INT, Nombre TEXT, Apellido TEXT)''')
cursor.execute('''INSERT INTO Alumnos VALUES(1, 'Alejandro', 'Pereira')''')
cursor.execute('''INSERT INTO Alumnos VALUES(2, 'Manuel', 'Rodriguez')''')
cursor.execute('''INSERT INTO Alumnos VALUES(3, 'Roberto', 'Pechofrio')''')
cursor.execute('''INSERT INTO Alumnos VALUES(4, 'Alejado', 'Distante')''')
cursor.execute('''INSERT INTO Alumnos VALUES(5, 'Alexios', 'Griego')''')
cursor.execute('''INSERT INTO Alumnos VALUES(6, 'Alejo', 'Alejadin')''')
cursor.execute('''INSERT INTO Alumnos VALUES(7, 'Alexander', 'Alex')''')
cursor.execute('''INSERT INTO Alumnos VALUES(8, 'Alex', 'Alexander')''')

tabla.commit()

cursor.execute('''SELECT * FROM Alumnos WHERE Apellido = 'Griego' ''')
rows = cursor.fetchall()
print(rows)

cursor.close()
tabla.close()