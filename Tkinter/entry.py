from tkinter import*
#Configuracion de la raiz
root= Tk()

label= Label(root, text="Nombre")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry = Entry(root)
entry.grid(row=0, column=1,padx=5, pady=5)
entry.config(justify="center")

label2 = Label(root, text="Apellido")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1,padx=5, pady=5)
entry2.config(justify="center")

label3 = Label(root, text="Email")
label3.grid(row=2, column=0, sticky="w", padx=5, pady=5)

entry3 = Entry(root)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry3.config(justify="center")

label4 = Label(root, text="Contraseña")
label4.grid(row=3, column=0, sticky="w", padx=5, pady=5)

entry4 = Entry(root)
entry4.grid(row=3, column=1,padx=5, pady=5)
entry4.config(justify="center",show="*")

#Bucle de la aplicacion
root.mainloop()