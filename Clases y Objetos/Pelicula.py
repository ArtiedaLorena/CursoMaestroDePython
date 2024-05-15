class Pelicula:
    #Contructor de clase
    def __init__ (self, titulo, duracion, lanzamiento):
        self.titulo= titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado una pelicula", self.titulo)
    # Destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula", self.titulo)

    def __str__(self):
        return f"{self.titulo} lanzada en {self.lanzamiento} con una duracion de {self.duracion} segundos"

    def __len__(self):
        return self.duracion
p = Pelicula("EL padrino", 175, 1972)

print(p)
del(p)




