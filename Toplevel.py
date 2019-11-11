"""
Cria uma Janela básica TopLevel do Tkinter.
"""
from tkinter import *


root = Tk()
root.title('Janela principal')
root.lift()
top = Toplevel()
top.title('TopLevel')
root.mainloop()
