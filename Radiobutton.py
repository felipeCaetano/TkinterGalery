"""
Cria Radiobutton sobre o objeto TK.
"""
from tkinter import *


root = Tk()
radiobutton0 = Radiobutton(root, text='Radiobutton 0', value=0).pack()
radiobutton1 = Radiobutton(root, text='Radiobutton 1', value=1).pack()

root.mainloop()
