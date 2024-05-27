from tkinter import *

def sumar():
    resultado.set(float(a.get()) + float(b.get()))
    borrar()

def restar():
    resultado.set(float(a.get()) - float(b.get()))
    borrar()

def multiplicar():
    resultado.set(float(a.get()) * float(b.get()))
    borrar()

def dividir():
    resultado.set(float(a.get()) / float(b.get()))
    borrar()

#Funcion para resetear los numeros ingresados
def borrar():
    a.set("")
    b.set("")

root = Tk()
root.config(background="light blue")
root.config(border=30)
root.geometry("380x320")
root.config(cursor="heart")
root.resizable(0, 0)

a = StringVar()
b = StringVar()
resultado = StringVar()

Label(root, text="Primer número", border=10, background="light blue").pack()
Entry(root, justify="center", textvariable=a).pack()  # Primer número
Label(root, text="Segundo número", border=10, background="light blue").pack()
Entry(root, justify="center", textvariable=b).pack()  # Segundo número

# Crear un frame para los botones
button_frame = Frame(root, background="light blue")
button_frame.pack(pady=10)  # Espaciado vertical entre los botones y las entradas

# Añadir botones al frame con espaciado
Button(button_frame, text="Sumar", command=sumar, width=8).pack(side="left", padx=5, pady=5)
Button(button_frame, text="Restar", command=restar, width=8).pack(side="left", padx=5, pady=5)
Button(button_frame, text="Multiplicar", command=multiplicar, width=8).pack(side="left", padx=5, pady=5)
Button(button_frame, text="Dividir", command=dividir, width=8).pack(side="left", padx=5, pady=5)

Label(root, text="RESULTADO", background="light blue").pack()
Entry(root, justify="center", textvariable=resultado, state="disabled").pack()

root.mainloop()