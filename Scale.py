"""
Cria um Slider sobre o objeto TK.
"""
from tkinter import *


root = Tk()
slider = Scale(root, from_=0, to=100).pack()
# na posição horizontal:
# horizontal_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL).pack()
root.mainloop()
