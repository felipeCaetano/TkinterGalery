"""
Cria um botão basico do Tkinter e o coloca na janela principal.
"""
from tkinter import *


root = Tk()
button = Button(root, text='Botão').pack()
root.mainloop()
