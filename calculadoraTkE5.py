
from tkinter import*
from tkinter import messagebox
import math
#---FUNCIONES---------------------------------------------------
def sumar():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        #labelResultado.grid()
     
        if valor1=="" or valor2=="":
            messagebox.showwarning("Error", "Falta ingresar valores")
        else:
            resultado=int(valor1) + int(valor2)
            labelResultado["text"]=resultado
            
            return sumar
    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")
#...................................................................................
def restar():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.grid()
     
        if valor1=="" or valor2=="":
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) - int(valor2)
            labelResultado["text"]=resultado
    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")
#....................................................................................
def multiplicar():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.grid()
     
        if valor1=="" or valor2=="":
            messagebox.showwarning("Error", "Ingrese un valor correcto")
        else:
            resultado=int(valor1) * int(valor2)
            labelResultado["text"]=resultado
    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")
#............................................................................................
def dividir():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.grid()
     
        if valor1=="" or valor2=="":
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) / int(valor2)
            labelResultado["text"]=resultado
    except:
        messagebox.showerror("Error", "No es posible dividir por cero")   
#......................................................................................
def porcentaje():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        #labelResultado.grid()
     
        if valor1=="" or valor2=="":
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) * int(valor2) / 100
            labelResultado["text"]=resultado
    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")  
#......................................................................................
def reset():
    valor=int(labelResultado["text"])
    labelResultado["text"]=0
    eValor1.delete(0, END)
    eValor2.delete(0, END)

#------------------------------------------------------------------------------------
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("+480+180")
ventana.rowconfigure([0,1], weight=1)
ventana.columnconfigure([0,1,2,3,4,5,6,7], weight=1)
labelValor1=Label(ventana, text="VALOR 1")
labelValor1.grid(row=0, column=0)
eValor1=Entry(ventana, bg="white")
eValor1.grid(row=0, column=1)
labelValor2=Label(ventana, text="VALOR 2")
labelValor2.grid(row=1, column=0)
eValor2=Entry(ventana, bg="white")
eValor2.grid(row=1, column=1)
Etiqueta3=Label(ventana, text="RESULTADO =")
Etiqueta3.grid(row=4, column=0)
labelResultado=Label(ventana, bg="light blue", width=17)
labelResultado.grid(row=4, column=1)

#---BOTONES------------------------------------------------------------
sumar=Button(ventana, text="+", command= sumar, width=15)
sumar.grid(row=6, column=0, sticky="nsew")
restar=Button(ventana, text="-", command=restar)
restar.grid(row=6, column=1, sticky="nsew")
multiplicar=Button(ventana, text="*", command=multiplicar)
multiplicar.grid(row=7, column=0, sticky="nsew")
dividir=Button(ventana, text="/", command=dividir)
dividir.grid(row=7, column=1, sticky="nsew")
porcentaje=Button(ventana, text="%", command=porcentaje)
porcentaje.grid(row=8, column=0, sticky="nsew")
clear=Button(ventana, text="Clear", bg="green", command=reset)
clear.grid(row=8, column=1, sticky="nsew")

ventana.mainloop()


