from HerenciaDeClases.Producto import Producto


class Adorno(Producto):
    def __init__(self, referencia, tipo, nombre, pvp,descripcion, productor, distribuidor):
        super().__init__(referencia, tipo, nombre, pvp)

        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return (f"Referencia: {self.referencia}\n"
                f"Tipo: {self.tipo}\n"
                f"Nombre: {self.nombre}\n"
                f"Pvp: {self.pvp}\n"
                f"Descipcion: {self.descripcion}\n"
                f"Productor: {self.productor}\n"
                f"Distribuidor: {self.distribuidor}")
    