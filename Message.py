"""
Cria uma menssagem sobre o objeto TK.
Message é um widget semelhante ao Lable mas que suporta multiplas linhas.
"""
from tkinter import *


root = Tk()
message = Message(root, text='Isso é uma mensagem relativamente longa').pack()
root.mainloop()
