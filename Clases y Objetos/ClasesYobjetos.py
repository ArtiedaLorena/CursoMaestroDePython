#La clase es como un molde para crar objtos
class Galletita:
    chocolate = False


#Instanciacion (creacion de un objeto)
una_galleta= Galletita()
otra_gallta= Galletita()
print(type(una_galleta))

una_galleta.sabor = "Salado"
una_galleta.color= "Marron"
print(una_galleta.sabor)
print(una_galleta.chocolate)

class Galletita():
    chocolate = False
    #Se comporta como un constructor, self hace referencia al propio objeto
    def __init__(self, sabor=none, color):
        self.sabor = color
        self.color = sabor
        print("Se acaba de crear una galleta "+ color + " y " + sabor)
    def cocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una galleta con chocolate")
        else:
            print("Soy una galleta sin chocolate")


g = Galletita("Naranja", "Marron")




