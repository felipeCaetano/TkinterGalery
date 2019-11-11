"""
Cria um Menu sobre o objeto TK.
"""
from tkinter import *


root = Tk()
menubar = Menu(root)
menufile = Menu(menubar)
menufile.add_command(label="Hello!")
menufile.add_command(label="Quit!", command=root.quit)
menubar.add_cascade(label="File", menu=menufile)
root.config(menu=menubar)
root.mainloop()
