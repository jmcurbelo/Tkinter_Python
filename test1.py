from tkinter import *

def clicked():

    muestra = Label(window, text = "")
    muestra.grid(column = 0, row = 4)
    muestra.configure(text= txt.get())



window = Tk()

window.geometry('450x300')    # Tamaño de la ventana

window.title("Welcome to LikeGeeks app") #Título de la ventana

lbl = Label(window, text="Entre lo que desea imprimir", font=("Arial Bold", 20))
lbl.grid(column = 0, row = 0)

txt = Entry(window,width=35)  #state = 'disabled' desabilita el campo
txt.grid(column = 0, row = 2)
txt.focus()                          # hace foco en la entrada para escribir

# Agregar un boton
btn = Button(window, text="Click Me", bg="green", fg="red", font=("Arial Bold", 15),
             command = clicked)

btn.grid(column=0, row=3, )

window.mainloop()

