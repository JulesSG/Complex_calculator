import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys

import OPERACIONES

ventana = tk.Tk()
ventana.title("Calculadora de complejos")
ventana.geometry("1200x400")
ventana.iconbitmap("icono.ico")
##############################################################

def cNum1():
    try:
        global polar1
        TXT_polar1.config(state=NORMAL)
        modulo=float(TXT_modulo.get())
        angulo=float(TXT_angulo.get())
        polar1=[modulo,angulo]
        TXT_polar1.insert(INSERT,f"{polar1[0]}@{polar1[1]}°")
        TXT_polar1.config(state=DISABLED)
    except ValueError:
        messagebox.showerror(message="Mae solo metale numeros, nada mas.", title="Error", )
        TXT_polar1.config(state=DISABLED)
#################################################################
def cNum2():
    try:
        global polar2
        TXT_polar2.config(state=NORMAL)
        modulo=float(TXT_modulo.get())
        angulo=float(TXT_angulo.get())
        polar2=[modulo,angulo]
        TXT_polar2.insert(INSERT,f"{polar2[0]}@{polar2[1]}°")
        TXT_polar2.config(state=DISABLED)
    except ValueError:
        messagebox.showerror(message="Mae solo metale numeros, nada mas.", title="Error", )
        TXT_polar2.config(state=DISABLED)
##################################################################
def cNum3():
    try:
        global polar3
        TXT_polar3.config(state=NORMAL)
        modulo=float(TXT_modulo.get())
        angulo=float(TXT_angulo.get())
        polar3=[modulo,angulo]
        TXT_polar3.insert(INSERT,f"{polar3[0]}@{polar3[1]}°")
        TXT_polar3.config(state=DISABLED)
    except ValueError:
        messagebox.showerror(message="Mae solo metale numeros, nada mas.", title="Error", )
        TXT_polar3.config(state=DISABLED)
#######################################################################
def sum_AB():
    resul=OPERACIONES.suma(polar1,polar2)
    TXT_resul.delete('1','end')
    TXT_resul.insert(INSERT,f"{resul[0]} @ {resul[1]}")
def sum_ABC():
    resul=OPERACIONES.suma(OPERACIONES.suma(polar1,polar2),polar3)
    TXT_resul.delete('1', 'end')
    TXT_resul.insert(INSERT, f"{resul[0]} @ {resul[1]}")
def mul_AB():
    resul=OPERACIONES.multiplicar(polar1,polar2)
    TXT_resul.delete('1', 'end')
    TXT_resul.insert(INSERT, f"{resul[0]} @ {resul[1]}")
#######################################################################
LB_modulo = Label(ventana, text="Modulo")
LB_modulo.grid(column=2, row=2)
TXT_modulo = Entry(ventana, width=20)
TXT_modulo.grid(column=3, row=2)
##############################################################
LB_angulo = Label(ventana, text="Angulo")
LB_angulo.grid(column=2, row=3)
TXT_angulo = Entry(ventana, width=20)
TXT_angulo.grid(column=3, row=3)
##############################################################
TXT_polar1=Entry(ventana, width=40)
TXT_polar1.place(x=25,y=60)
TXT_polar1.config(state=DISABLED)
##############################################################
TXT_polar2=Entry(ventana, width=40)
TXT_polar2.place(x=25,y=90)
TXT_polar2.config(state=DISABLED)
##############################################################
TXT_polar3=Entry(ventana, width=40)
TXT_polar3.place(x=25,y=120)
TXT_polar3.config(state=DISABLED)
##############################################################
BTN_polar1 = Button(ventana, text="A",command=cNum1)
BTN_polar1.place(x=2,y=60)
##############################################################
BTN_polar2=Button(ventana, text="B",command=cNum2)
BTN_polar2.place(x=2,y=90)
########################################################
BTN_polar3=Button(ventana, text="C",command=cNum3)
BTN_polar3.place(x=2,y=120)
################################################################
#Sumar los complejos
##############################
#sumar A Con B
BTN_AB = Button(ventana,text='A+B', command=sum_AB)
BTN_AB.place(x=400)
#Sumar A+B+C
BTN_ABC = Button(ventana,text='A+B+C', command=sum_ABC)
BTN_ABC.place(x=500)
#multiplicar A*B
BTN_AB = Button(ventana,text='A*B', command=mul_AB)
BTN_AB.place(x=600)
#Resultado
LB_resultado = Label(ventana, text="Resultado")
LB_resultado.place(x=400,y=50)
TXT_resul = Entry(ventana, width=50, )
TXT_resul.place(x=400,y=80,height=100)
ventana.mainloop()

