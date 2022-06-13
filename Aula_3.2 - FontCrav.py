from tkinter import *
from turtle import right

janela = Tk();#declara uma instância da função TK()

a = Button(janela, text='vermelho',fg='#8A39E1')#atribui um botão a variável
a.pack(side=LEFT)
b = Button(janela,text='verde',fg='#9C51E0')
b.pack(side=TOP)
c=Button(janela, text='azul',fg='#B667F1')
c.pack(side=BOTTOM)
d = Button(janela, text='Chave',fg='#ECC488')
d.pack(side=RIGHT)

#pack não há uma sobreposição dos elementos
janela.mainloop() 