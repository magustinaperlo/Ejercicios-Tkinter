from faulthandler import disable
from tkinter import *
from random import *
#-----------------------------------------------------

def generarAleatorios():
    if int(variable1.get()) > int(variable2.get()):
        nroRan=str(randint(int(variable2.get()), int(variable1.get())))
        numero.set(nroRan)
    elif int(variable1.get()) < int(variable2.get()):
        nroRan=str(randint(int(variable1.get()), int(variable2.get())))
        numero.set(nroRan)
#------------------------------------------------------   
ventana=Tk()
ventana.geometry("500x280")
ventana.resizable(width=FALSE, height=FALSE)
ventana.title("Generador de números")
ventana.config(bg="LightSteelBlue3")

numero1=Label(ventana, text="Número 1", bg="LightSteelBlue3", font="arial, 13").place(x=98, y=40)
numero2=Label(ventana, text="Número 2", bg="LightSteelBlue3", font="arial, 13").place(x=98, y=100)

variable1=StringVar()
variable2=StringVar()

spin1=Spinbox(ventana, from_=0, to=100000000, font="arial, 13", width=16, bg="deepskyblue3", bd=4, textvariable=variable1)
spin1.place(x=218, y=100)
spin2=Spinbox(ventana, from_=0, to=100000000, font="arial, 13", width=16, bg="deepskyblue3", bd=4, textvariable=variable2)
spin2.place(x=218, y=40)

nroGenerado=Label(ventana, text="Número generado", bg="LightSteelBlue3", font="arial, 13").place(x=65, y=160)

numero=StringVar()
ventanaNroGen=Label(ventana, font="arial, 13", width=17, textvariable=numero, bg="deepskyblue3").place(x=220, y=160)

botonGenerar=Button(ventana, text="generar", font="verdana, 12", bg="deepskyblue3", bd=4, command=generarAleatorios)
botonGenerar.place(x=264, y=210)

ventana.mainloop()