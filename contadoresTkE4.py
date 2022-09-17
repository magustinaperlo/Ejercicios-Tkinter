from tkinter import *
#-------------------------------------------------------------------------------------
def decremetar():
    valor=int(etiquetaValor["text"])
    etiquetaValor["text"]=f"{valor-1}"

def incremetar():
    valor=int(etiquetaValor["text"])
    etiquetaValor["text"]=f"{valor+1}"

def reset():
    valor=int(etiquetaValor["text"])
    etiquetaValor["text"]=0
#--------------------------------------------------------------------------------------
ventana=Tk()
ventana.title("Contador")
ventana.rowconfigure(0, minsize=50, weight=1)
ventana.columnconfigure([0,1,2,3,4], minsize=50, weight=1)
etiquetaCont=Label(ventana, text="Contador =", font="bold").grid(row=0, column=0)
etiquetaValor=Label(ventana, text="0", font="bold")
etiquetaValor.grid(row=0, column=1)
botonDecrementar=Button(ventana, text="DOWN -", command=decremetar, bg="red")
botonDecrementar.grid(row=0, column=2, sticky="nsew")
botonIncrementar=Button(ventana, text="UP +", command=incremetar, bg="yellow")
botonIncrementar.grid(row=0, column=3, sticky="nsew")
botonReset=Button(ventana, text="RESET", command=reset, bg="green")
botonReset.grid(row=0, column=4, sticky="nsew")
#--------------------------------------------------------------------------------------
ventana.mainloop()