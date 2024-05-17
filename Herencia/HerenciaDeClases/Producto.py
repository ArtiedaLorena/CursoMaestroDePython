import copy
class Producto:
    def __init__(self, referencia, tipo, nombre, pvp):
        self.referencia = referencia
        self.tipo= tipo
        self.nombre=nombre
        self.pvp= pvp


    def rebajar_producto(self, p, rebaja):
        self.p= p
        p.pvp = p.pvp - (p.pvp/100 * rebaja)
        return p
        
    def __str__(self):
        return (f"Referencia: {self.referencia}\n"
                f"Tipo: {self.tipo}\n"
                f"Nombre: {self.nombre}\n"
                f"Pvp: {self.pvp}")

