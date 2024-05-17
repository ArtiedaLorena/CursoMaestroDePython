from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Coche\n"+super().__str__() + f"\nVelocidad: {self.velocidad} Km/h\nCilindrada: {self.cilindrada}"