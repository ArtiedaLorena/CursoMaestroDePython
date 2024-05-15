import math


class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x} ,{self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            print("Origen")
        elif self.x >= 0 and self.y >= 0:
            print("Primer cuadrante")
        elif self.x <= 0 <= self.y:
            print("Segundo cuadrante")
        elif self.x <= 0 and self.y <= 0:
            print("Tercer cuadrante")
        elif self.x >= 0 and self.y >= 0:
            print("Cuarto cuadrante")
        else:
            print("Valores erroneos")

    def vector(self, p):

        return f"El vector es: ({p.x - self.x}, {p.y - self.y})"

    def distancia(self, p):
        distancia = math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
        return f"La distancia entre los dos punto es: {distancia}"

#Pruebas

A = Punto(2,3)
B=Punto(5,5)
C= Punto(-3,-1)
D=Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

print(A.vector(B))
print(B.vector(A))

print(A.distancia(B))
print(B.distancia(A))

print(A.distancia(D))
print(B.distancia(D))
print(C.distancia(D))




