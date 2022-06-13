#importaçoes de bibliotecas
from cProfile import label
from decimal import Rounded
from email.utils import collapse_rfc2231_value
from struct import pack
from tkinter import*
from tkinter import ttk
from turtle import width

#const das cores
cor0='#3D018C'
cor1='#7E1CFF'
cor2='#5F02D9'
cor3='#8C8900'
cor4='#D9D402'

#criando a janela
janela= Tk()
janela.title('IMC')
janela.geometry('600x600')
janela.configure(bg='#7E1CFF')

#dividindo a janela em frames

#conjunto de frames superiores

frame_sup=Frame(janela, width=600, height=100, bg=cor0, padx=0, pady=0, relief='flat')
frame_sup.grid(row=0, column=0, sticky=NSEW)

tittulo=Label(frame_sup, text="Calculo do IMC", width=40, height=2, padx=0, relief="flat",anchor="center", font=("Ivy 16 bold"),bg=cor0, fg=cor4)
tittulo.place(in_=frame_sup, anchor="c",relx=0.5, rely=0.5)

#calculo
def calcular():
    massa= float(e_massa.get())
    altura = float(e_altura.get())

    imc = massa/altura**2

    resultado = imc

    if resultado < 18.5:
        #print("Seu IMC está a baixo do esperado")
        l_resultado_texto ['text'] = "Magro"
    elif resultado>=18.5 and resultado < 25:
        l_resultado_texto ['text'] = "Normal"
    elif resultado>=25 and resultado < 30:
        l_resultado_texto ['text'] = "Gordo"     
    else:
        l_resultado_texto ['text'] = "Obeso"

    l_resultado['text'] =  "{:.{}f}".format(resultado,2)
    print(resultado)
 
#conjunto de frames do meio

frame_med=Frame(janela, width=600, height=250, bg=cor2, padx=0, pady=0, relief='flat')
frame_med.grid(row=1, column=0, sticky=NSEW)

titulo_2=Label(frame_med, text="Para calculo do IMC (Índice de Massa Corporal), preencha os campos abaixo:", width=100, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 9 bold"),bg=cor2, fg=cor4)
titulo_2.place(in_=frame_med, anchor="c",relx=0.5, rely=0.1)

label_massa =Label(frame_med, text="Seu peso:", bg=cor2, fg=cor4)
label_massa.place(in_=frame_med, anchor="w",relx=0, rely=0.8)
e_massa =  Entry(janela, width= 10)
e_massa.place(in_=frame_med, anchor="c",relx=0.5, rely=0.8)

label_altura =Label(frame_med, text="Sua altura:", bg=cor2, fg=cor4)
label_altura.place(in_=frame_med, anchor="w",relx=0, rely=0.4)
e_altura =  Entry(janela, width= 10)
e_altura.place(in_=frame_med, anchor="c",relx=0.5, rely=0.4)


l_resultado=Label(frame_med,text="---",width=12, height=6,padx=6, pady=12,relief='flat',anchor='center',font=('Ivy 15 bold'), bg=cor1, fg=cor4)
l_resultado.place(in_=frame_med, anchor="w",relx=0.7, rely=0.6)

l_resultado_texto=Label(frame_med,text="",width=12, height=1, padx=3, pady=2,relief='flat',anchor='center',font=('Ivy 8 bold'), bg=cor1, fg=cor4)
l_resultado_texto.place(in_=frame_med, anchor="c",relx=0.84, rely=0.85)

#conjunto de frames de baixo

frame_bot=Frame(janela, width=600, height=250, bg=cor1, padx=0, pady=0, relief='flat')
frame_bot.grid(row=2, column=0, sticky=NSEW, pady=15, padx=2)

calcular=Button(frame_bot, command=calcular, text='Calcular', width=45,height=1, overrelief="solid", anchor='center', font=('Ivy 12 bold'), bg=cor2, fg=cor4)
calcular.place(in_=frame_bot, anchor="c" ,relx=0.5, rely=0.5)

janela.mainloop()