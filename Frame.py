"""
Um Frame dentro da janela raiz.
Perceba que o frame vazio tem tamanho minimo possível
"""
from tkinter import *


root = Tk()
frame = Frame(root).pack()
root.mainloop()
