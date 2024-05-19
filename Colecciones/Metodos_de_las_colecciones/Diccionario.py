colores={"Amarillo":"Yellow","Azul":"Blue","Verde":"Green"}
#Devuelve el valor de la clave pasada
print(colores["Amarillo"])

#Get devuelve la clave del valor pasado
print(colores.get("Amarillo","No se encuentra"))
#Recorre el diccionario y nos dice si el elemento se encuentra o no
print("Amarillo" in colores)

#Devuelve una lista con las claves del Diccionario
colores.keys()