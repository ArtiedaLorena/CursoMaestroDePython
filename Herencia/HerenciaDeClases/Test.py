from HerenciaDeClases.Adorno import Adorno
from HerenciaDeClases.Alimento import Alimento
from HerenciaDeClases.Libro import Libro
import copy


class Test:
    adorno= Adorno("0004","Maceta", "Maceta de ceramica", 15, "Maceta de ceramica para decoracion", "ArtDeco", "Ceramiquit")
    alimento = Alimento("00345", "Pan de masa madre", "Pan Madre", 134, "Bimbo", "Panettone")
    libro = Libro("0983", "Libro de bolsillo", "La casa de los espiritus", 90, "57689", "Isabel Allende")
    print(adorno)
    print(alimento)
    print(libro)

    productos=(adorno,alimento,libro)

    for p in productos:
        if(isinstance(p,Adorno)):
            print(p.referencia, p.nombre, p.distribuidor)
        elif(isinstance(p, Alimento)):
            print(p.referencia, p.nombre, p.productor)
        elif(isinstance(p, Libro)):
            print(p.referencia, p.nombre, p.autor)

    #Uso de Copy para no sobreescribir el producto original y aplicarle el descuento
    adorno_rebajado= copy.copy(adorno)
    print(adorno_rebajado)
    adorno_rebajado.rebajar_producto(adorno_rebajado, 50)
    print(adorno_rebajado)