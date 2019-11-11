"""
Cria a Janela básica do Tkinter - o objeto TK.
"""
from tkinter import *


root = Tk()
scrollbar = Scrollbar(root).pack()
# scrollbar = Scrollbar(root, orient=HORIZONTAL).pack()
root.mainloop()
