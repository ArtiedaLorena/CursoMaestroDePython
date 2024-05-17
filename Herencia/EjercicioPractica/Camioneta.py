from Coche import Coche
from Vehiculo import Vehiculo


class Camioneta(Vehiculo):
    def __init__(self,color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga=carga


    def __str__(self):
        return("Camioneta\n"+ super().__str__()+ f"\nCarga: {self.carga}Kg")

