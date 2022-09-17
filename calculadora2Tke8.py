from tkinter import *
from unittest import result
#...................................................................

def calcular():
    if varOpcion.get() == 1:
         resultado=int(boxValor1.get())+int(boxValor2.get())
    elif varOpcion.get() == 2:
        resultado=int(boxValor1.get())-int(boxValor2.get())
    elif varOpcion.get() == 3:
        resultado=int(boxValor1.get())*int(boxValor2.get())
    elif varOpcion.get() == 4:
        if int(boxValor2.get())==0:
            resultado="No se puede / por cero"
            variableResultado.set(resultado)
        else:
            resultado=int(boxValor1.get())/int(boxValor2.get())
    else:
        resultado ="Complete las opciones"
    variableResultado.set(resultado)
 
 #..................................................................   

ventana=Tk()
ventana.geometry("500x280")
ventana.resizable(width=FALSE, height=FALSE)
ventana.title("calculadora 2")
ventana.config(bg="gray32")

valor1=Label(ventana, text="VALOR 1", bg="gray32", font="verdana, 13", fg="lawn green").place(x=30, y=60)
valor2=Label(ventana, text="VALOR 2", bg="gray32", font="verdana, 13", fg="lawn green").place(x=30, y=110)
labelResultado=Label(ventana, text="RESULTADO", bg="gray32", font="verdana, 11", fg="lawn green").place(x=30, y=163)
labelOperacion=Label(ventana, text="OPERACIONES", bg="gray32", font="verdana, 11", fg="lawn green").place(x=349, y=25)

boxValor1=Entry(ventana)
boxValor1.place(x=160, y=65)
boxValor2=Entry(ventana)
boxValor2.place(x=160, y=115)
variableResultado=StringVar()
boxResultado=Entry(ventana, textvariable=variableResultado)
boxResultado.place(x=160, y=165)

varOpcion=IntVar()
suma=Radiobutton(ventana, text="Sumar", variable=varOpcion, value=1, font="verdana, 13", fg="green3", bg="gray32")
suma.place(x=355, y=60)
resta=Radiobutton(ventana, text="Resar", variable=varOpcion, value=2, font="verdana, 13", fg="green3", bg="gray32")
resta.place(x=355, y=95)
producto=Radiobutton(ventana, text="Multiplicar", variable=varOpcion, value=3, font="verdana, 13", fg="green3", bg="gray32")
producto.place(x=355, y=130)
division=Radiobutton(ventana, text="Dividir", variable=varOpcion, value=4, font="verdana, 13", fg="green3", bg="gray32")
division.place(x=355, y=165)

calcular=Button(ventana, text="CALCULAR", command=calcular, font="verdana, 10", fg="lawn green", bg="gray32", bd=3)
calcular.place(x=175, y=210)

ventana.mainloop()