"""
Cria um combobox (Select) sobre o objeto TK.
O widget Combobox está definido dentro de ttk
"""
from tkinter import *
from tkinter import ttk


root = Tk()
combobox = ttk.Combobox(root, values=['Escolha um item:']).pack()
root.mainloop()
