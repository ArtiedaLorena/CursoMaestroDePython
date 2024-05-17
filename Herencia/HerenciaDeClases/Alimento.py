from HerenciaDeClases.Producto import Producto


class Alimento(Producto):
    def __init__(self, referencia, tipo, nombre, pvp, productor, distribuidor):
        super().__init__(referencia, tipo, nombre, pvp)
        self.productor= productor
        self.distribuidor= distribuidor


    def __str__(self):
        return (f"Referencia: {self.referencia}\n"
                f"Tipo: {self.tipo}\n"
                f"Nombre: {self.nombre}\n"
                f"Pvp: {self.pvp}\n"
                f"Productor: {self.productor}\n"
                f"Distribuidor: {self.distribuidor}")
