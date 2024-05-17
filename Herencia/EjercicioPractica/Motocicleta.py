from Bicicleta import Bicicleta


class Motocicleta(Bicicleta):
    def __init__(self,color, ruedas,tipo,velocidad, cilindrada):
        super().__init__(color, ruedas,tipo)
        self.velocidad= velocidad
        self.cilindrada= cilindrada

    def __str__(self):
        return("Motocicleta\n"+super().__str__()+(f"\nVelocidad: {self.velocidad}Km/h\n"+ f"Cilindrada: {self.cilindrada}cc"))
