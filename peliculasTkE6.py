from tkinter import *
from tkinter import messagebox
#---------------------------------------------------------------------
def añadir():
    #validacion para campo vacio
    a=ingresoPelicula.get()
    if (a.isspace() or len(a) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
        ingresoPelicula.delete(0, END)
    else:
        widgetPelidIngresadas.insert(END, a) #Se inserta en Listbox
        ingresoPelicula.delete(0, END) #Se limpia el campo
    
    

#---------------------------------------------------------------------
ventana=Tk()
ventana.geometry("500x300")
ventana.resizable(width=FALSE, height=FALSE)
ventana.title("Peliculas")
ventana.config(bg="DarkSeaGreen")
tituloPelicula=Label(ventana, text="Escribe el título de una película", bg="GreenYellow", font="verdana, 11")
tituloPelicula.place(x=15, y=32)
peliculas=Label(ventana, text="Películas", bg="GreenYellow", font="verdana")
peliculas.place(x=318, y=30)
ingresoPelicula=Entry(ventana, bg="lavender", bd=3, font="verdana, 11")
ingresoPelicula.place(x=26, y=80, width=180, height=30)
botonAñadir=Button(ventana, text="añadir", font="verdana, 11", bg="GreenYellow", bd=3, command=añadir)
botonAñadir.place(x=90, y=130)
widgetPelidIngresadas=Listbox(ventana, bg="lavender", bd=2, font="verdana, 11")
widgetPelidIngresadas.place (x=250, y=60, width=210)
#-----------------------------------------------------------------

ventana.mainloop()
