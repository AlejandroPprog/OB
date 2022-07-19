import tkinter
from tkinter import StringVar, ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title('Ejercicio 1')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
selected = tkinter.StringVar()
#Esto genera una ventana emergente
def elegido():
    messagebox.showinfo(f'OP {str(selected.get())}', f'Yo soy el elegido, la opción {str(selected.get())}')

def Reinicio(event):
    selected.set(None)

def Salir(event):
    window.quit()

opcion1 = ttk.Radiobutton(window, text='Soy la opción 1', value=1, variable=selected, command=elegido)
opcion2 = ttk.Radiobutton(window, text='Soy la opción 2', value=2, variable=selected, command=elegido)
opcion3 = ttk.Radiobutton(window, text='Soy la opción 3', value=3, variable=selected, command=elegido)

botonReinicio = tkinter.Button(window, text='Estoy para reiniciarlo todo')
botonReinicio.bind('<Button-1>', Reinicio)
botonSalir = tkinter.Button(window, text='Salir')
botonSalir.bind('<Button-1>', Salir)

opcion1.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
opcion2.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
opcion3.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
botonReinicio.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)
botonSalir.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()