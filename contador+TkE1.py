from tkinter import *

def incremetar():
    valor=int(lineEdit["text"])
    lineEdit["text"]=f"{valor+1}"

ventana=Tk()
ventana.title("Contador Creciente")
ventana.geometry("+250+150")
ventana.rowconfigure(0, minsize=35, weight=1)
ventana.columnconfigure([0,1,2], minsize=35, weight=1)
etiquetaContador=Label(ventana, text="Contador").grid(row=0, column=0)
lineEdit=Label(ventana, text="0", bg="yellow")
lineEdit.grid(row=0, column=1)
botonMas=Button(ventana, text="+", command=incremetar).grid(row=0, column=2)


ventana.mainloop()



