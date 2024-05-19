from Bicicleta import Bicicleta
from Camioneta import Camioneta
from Coche import Coche
from Motocicleta import Motocicleta


class Test:
    bicicleta1= Bicicleta("Rojo",2, "Paseo")
    camioneta1= Camioneta("Blanco", 4, 2000)
    motocicleta1 = Motocicleta("Verde", 2,"paseo",180, 1.0)
    coche1= Coche("Azul",4, 250, 2.5)

    vehiculos=(bicicleta1,camioneta1,motocicleta1,coche1)


    for v in vehiculos:
        print(v,"\n")

    def catalogar(listaVehiculos, ruedas):
        for v in listaVehiculos:
            if v.ruedas == ruedas:
                print(type(v).__name__)

    catalogar(vehiculos, 2)

