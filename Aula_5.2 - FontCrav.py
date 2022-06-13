from tkinter import *
from tkinter.ttk import *

wd=Tk()
wd.title('aula 5.2')
wd.geometry('300x200')
wd.configure(bg='#b1d8ff')

estado = StringVar()

def test():
    print('Olá, estou', estado.get())

check = Checkbutton(wd,text='Olá? Tudo bem ou não?',var=estado,
                            onvalue="Bem",offvalue="Não",command=test)
check.grid(row=1,column=1)



wd.mainloop()