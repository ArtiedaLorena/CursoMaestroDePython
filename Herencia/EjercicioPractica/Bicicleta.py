from Vehiculo import Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self,color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

    def __str__(self):
        return("Bicicleta\n"+super().__str__()+ f"\nTipo: {self.tipo}")


