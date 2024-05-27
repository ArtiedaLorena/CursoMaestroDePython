from tkinter import *
#Configuracion de la raiz
root = Tk()

#Configuracion de un marco
#frame = Frame(root,width=480, height=320)
#frame.pack()

'''label = Label(root, text="SUR").pack(anchor="sw")
label = Label(root, text="Norte").pack(anchor="nw")
label = Label(root, text="Hola mundo").pack()
'''
imagen= PhotoImage(file="gifanimado.gif")
Label(root, image=imagen, bd=0).pack()
#Finalmente bucle de la aplicacion
root.mainloop()

