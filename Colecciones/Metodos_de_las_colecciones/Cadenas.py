print("Hola mundo".lower())
print("Hola mundo".capitalize())
print("Hola mundo".title())
print("Hola mundo".count("mundo"))
print("Hola mundo".find("mundo"))

#Revese find, busqueda al revez busca la ultima
# palabra que se repite y nos devuelve el
# indice donde empieza
print("Hola mundo mundo mundo".rfind("mundo"))

#Is digit nos devuelve verdadero porque todos los caracteres son numeros

c= "100"
c.isdigit()
c2= "abc1234AS"
#Is alpha numerico: devuelve true si los caracteres son letras o numeros
c2.isalnum()
#Is Alpha: todas letras
c2.isalpha()
print("Hola mundo".islower())
print("HOLA MUNDO".isupper())
print("Hola Mundo".istitle())
print("Hola mundo".startswith("H"))
print("Hola mundo".endswith("o"))
#Split separa las palabras en una lista
print("Hola mundo".split())
#Separa la cadena con comas
print(",".join("Hola mundo"))
#Quita los espacios
print("             h             ".strip())
#Replace reemplaza lo que le pasamos por parametro en la cadena que le pasamos
print("Hola mundo".replace("mundo","Argentina"))
print("Hola mundo mundo mundo mundo".replace(" mundo", "",3))