from tkinter import *

root = Tk()
root.title("Hola mundo")
root.iconbitmap() #Icono
root.resizable(False, False) #Se puede redimensionar si tiene True si, sino no

#Frame
frame= Frame(root)
frame.pack()
frame.config(width=480, height=320)
frame.config(cursor="pirate")
frame.config(bg="green")
frame.config(bd=30)
frame.config(relief="sunken")


root.mainloop()


