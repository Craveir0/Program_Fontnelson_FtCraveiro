from tkinter import *
janela = Tk()
#cria o objeto janela
janela.title('Cainho')
#nome da janela  aberta
janela.geometry('280x218')
#fixa a resolução da janela
label = Label(janela, text='Fontenelle perde a OBR')
label.grid(column = 18,row = 8)
janela.mainloop()
#mantém a janela aberta 