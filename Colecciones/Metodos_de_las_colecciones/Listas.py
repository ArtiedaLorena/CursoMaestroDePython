lista = [1,2,3,4,5]
print(lista)
#Append: Añadimos un elemento al final de la lista
lista.append(6)
print(lista)
#lista.clear()
print(lista)
l2= [9,8,7]
#Reverse para dar vuelta una cadena
l2.reverse()
lista.extend(l2)
print(lista)
#Count devuelve la veces que se repite un elemento
["Hola", "Mundo", "Mundo"].count("Mundo")
#Index: nos devuelve el indice donde esta el elemento pasado por argumento
["Hola", "Mundo", "Mundo"].index("Mundo")
l=[1,2,3]
#Inserta un elemento en el indice indicado
l.insert(0,0)
print(l)
l=[0,5,10,15,25]
l.insert(3,20)
print(l)
#Insert para concatenar cadenas, insertamso una lista en la otra
l.insert(len(l),30)
print(l)
#Pop SIN argumento elimina el ultimo indice
l.pop()
#Pop con argumento elimina el elemento del indice pasado
l.pop(3)
print(l)
#Remove para eliminar un elemento en especial
l.remove(10)
#Para dar vuelvta una cadena, como no sepuede con reverse
#Primero lo asignamos a una lista, lueg lo damos vuelta y por ultimo volvemos a convertirlo a srt
l = list("Hola mundo")
print(l)
l.reverse()
cadena = "".join(l)
print (cadena)

l2 = [3,7,2,9]
#SORT ordena la cadena
l2.sort()
print(l2)
#Ordenamos una lsita al reves de mayor a menor
l2.sort(reverse=True)
