import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
label1 = tkinter.Label(window, text='Lista de fruta(o verdura)', bg='Yellow', fg='Black')
listaNumeros = ['Cacao', 'Uva', 'Platano', 'Tomate', 'Piña']
listaItems = tkinter.StringVar(value=listaNumeros)
listbox = tkinter.Listbox(window, height=10, listvariable=listaItems, bg='Black', fg='White')

listbox.pack(ipadx=30, ipady=30)
label1.pack(ipadx=30, ipady=30, side='top')

window.mainloop()