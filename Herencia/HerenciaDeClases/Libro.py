from HerenciaDeClases.Producto import Producto


class Libro(Producto):
    def __init__(self, referencia, tipo, nombre, pvp, isbn, autor):
        super().__init__(referencia, tipo, nombre, pvp)
        self.isbn=isbn
        self.autor=autor

    def __str__(self):
        return(f"Referencia: {self.referencia}\n"
                f"Tipo: {self.tipo}\n"
                f"Nombre: {self.nombre}\n"
                f"Pvp: {self.pvp}\n"
               f"ISBN: {self.isbn}\n"
               f"Ator: {self.autor}")