class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion= duracion
        self.lanzamiento = lanzamiento

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    peliculas = []
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
    def agregar (self,p):
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)

p2 = Pelicula("El resplandor", 260, 1975)

catalogo = Catalogo([p2])
catalogo.mostrar()

catalogo.agregar(Pelicula("El padrino", 206, 1976))

catalogo.mostrar()

