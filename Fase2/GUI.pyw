#*************************************
#Universidad del Valle de Guatemala
#Algoritmos y estructura de datos
#David Valenzuela       171001
#Marcos Gutierrez       17
#Fernando Hengstenberg  17699
#VacationDestination
#*************************************

#importamos libreria para GUI
from tkinter import *

#**************************Funcion Buscar************************
def vBuscar():
    #creamos una nueva ventana
    raiz.iconify()
    buscar=Tk()
    buscar.title("Buscar")
    #no ampliable raiz
    buscar.resizable(0,0)
    #tamaño de raiz
    buscar.geometry("700x500")
    #color de fondo de raiz
    buscar.config(bg="azure")
    #icono de raiz
    buscar.iconbitmap("icono.ico")


    
    #loop
    buscar.mainloop()
    

#****************************************************************



#**************************Funcion Agregar************************
def vAgregar():
    #creamos una nueva ventana
    raiz.iconify()
    agregar=Tk()
    agregar.title("Agregar")
    #no ampliable raiz
    agregar.resizable(0,0)
    #tamaño de raiz
    agregar.geometry("700x500")
    #color de fondo de raiz
    agregar.config(bg="azure")
    #icono de raiz
    agregar.iconbitmap("icono.ico")


    
    #loop
    agregar.mainloop()
    

#****************************************************************


#**************************Funcion Eliminar************************
def vEliminar():
    #creamos una nueva ventana
    raiz.iconify()
    eliminar=Tk()
    eliminar.title("Eliminar")
    #no ampliable raiz
    eliminar.resizable(0,0)
    #tamaño de raiz
    eliminar.geometry("700x500")
    #color de fondo de raiz
    eliminar.config(bg="azure")
    #icono de raiz
    eliminar.iconbitmap("icono.ico")


    
    #loop
    eliminar.mainloop()
    

#****************************************************************


#**************************Raiz************************
#creamos la raiz
raiz=Tk()
#titulo de rauz
raiz.title("vacatioin Destination")
#no ampliable raiz
raiz.resizable(0,0)
#tamaño de raiz
raiz.geometry("700x500")
#color de fondo de raiz
raiz.config(bg="azure")
#icono de raiz
raiz.iconbitmap("icono.ico")
#********************************************************


#**********************FramebtEliminar*******************
#Frame de boton eliminar
framebtE=Frame()
#lugar del frame
framebtE.pack(side="left", anchor="s")
#tamaño
framebtE.config(width="233",height="65")
#color
framebtE.config(bg="yellowgreen")
#********************************************************


#************************botonEliiminar******************
#agregar boton
btEliminar=Button(framebtE, text="Eliminar",command=vEliminar)

#lugar del boton
btEliminar.place(relwidth=0.8,relheight=0.8)
#********************************************************


#**************************FrameAgregar******************
#creamos un Frame
framebtA=Frame()
#empaquetamos en Frame
#lugar del Frame
framebtA.pack(side="right", anchor="s")
#color de fondo
framebtA.config(bg="yellowgreen")
#tamaño al Frame
framebtA.config(width="233", height="65")
#*********************************************************


#**************************Boton Agregar******************
#boton de Agregar
btAgregar=Button(framebtA, text="Agregar",command=vAgregar)
btAgregar.grid(column=1, row=1)
#lugar del boton
btAgregar.place(relwidth=0.8,relheight=0.8)
#*********************************************************


#**************************FrameBuscar******************
#creamos un Frame
framebtB=Frame()
#empaquetamos en Frame
#lugar del Frame
framebtB.pack(side="bottom")
#color de fondo
framebtB.config(bg="yellowgreen")
#tamaño al Frame
framebtB.config(width="234.5", height="65")
#*********************************************************


#**************************Boton Buscar******************
#boton de Agregar
btBuscar=Button(framebtB, text="Buscar",command=vBuscar)
btBuscar.grid(column=1, row=1)
#lugar del boton
btBuscar.place(relwidth=0.8,relheight=0.8)
#*********************************************************











#loop 
raiz.mainloop()
