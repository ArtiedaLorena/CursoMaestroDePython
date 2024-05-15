from Punto import Punto

class Rectangulo(Punto):
    def __init__(self, punto1=Punto(), punto2=Punto()):
        super().__init__()
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        base= int(abs(self.punto1.x - self.punto2.x))
        print(f"La base es: {base}")

    def altura(self):
        altura= int(abs(self.punto1.y - self.punto2.y))
        print(f"La altura es: {altura}")
    def area(self):
        self.base= int(abs(self.punto1.x - self.punto2.x))
        self.altura=int(abs(self.punto1.y - self.punto2.y))
        area= self.base * self.altura
        print(f"El area es: {area}")

#Pruebas
p1=Punto(2,3)
p2=Punto(5,5)
r = Rectangulo(p1,p2)

r.base()
r.altura()
r.area()

