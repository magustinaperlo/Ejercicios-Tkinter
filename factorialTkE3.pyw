from tkinter import *


def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)

def Obtener_Fact():
    print ("El factorial del número : "),numero.get()," es ",Factorial(numero.get())
    res=Factorial(numero.get())
    lblt=Label(Formulario1, text="Resultado: "+str(res))
    lblt.grid(row=2,column=0)
    
#------------------------------------------------------------------------------------------
Formulario1=Tk()
Formulario1.title('Factorial')
Formulario1.geometry('250x100')
#Formulario1.resizable(width=FALSE, height=FALSE)
#------------------------------------------------------------------------------------------
Etiqueta=Label(Formulario1, text="Factorial del número")
Etiqueta.grid()
numero=IntVar()
txtnumero=Entry(Formulario1, textvariable=numero, width=15)
txtnumero.grid(row=1, column=0)
BotonCalcula=Button(Formulario1, text="Calcular", command=Obtener_Fact, width=10)
BotonCalcula.grid(row=1, column=1)
#------------------------------------------------------------------------------------------
Formulario1.mainloop()
#------------------------------------------------------------------------------------------