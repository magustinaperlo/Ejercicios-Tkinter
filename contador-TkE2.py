from tkinter import *

def decremetar():
    valor=int(lineEdit["text"])
    lineEdit["text"]=f"{valor-1}"

ventana=Tk()
ventana.title("Contador Decreciente")
#fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
ventana.minsize(400, 150) 
ventana.maxsize(400, 150)
ventana.rowconfigure(0, minsize=35, weight=1)
ventana.columnconfigure([0,1,2], minsize=35, weight=1)
etiquetaContador=Label(ventana, text="Contador").grid(row=0, column=0)
lineEdit=Label(ventana, text="88", bg="orange")
lineEdit.grid(row=0, column=1)
botonMas=Button(ventana, text="-", command=decremetar).grid(row=0, column=2)


ventana.mainloop()
