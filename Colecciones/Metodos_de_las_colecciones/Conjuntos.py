c=set()#Declaracion del conjunto
c.add(1)
c.add(2)
c.add(3)
c.add(4)
print(c)
#Discard borra un elemento, sin argumento elimina el ultimo
c.discard(2)
print(c)
c2 = c.copy()
print(c2)
c2.discard(3)
print(c2)
print(c)
#Clear: Limpia el conjunto borrando todos sus elementos
# c.clear()
c1={1,2,3}
c2={3,4,5}
c3={-1,99,8}
c4={1,2,3,4,5}
#IsDisjunt devuelve true si los conjuntos son diferentes y false  si tienen elementos en comun
print(c2.isdisjoint(c1))
#IsSubset devuelve true si es un subconjunto del parametro pasado por argumento
print(c1.issubset(c4))
print(c3.issubset(c4))
#IsSuperSet devuelve true si es un superconjunto que contiene el elmento pasado po argumento
print(c4.issuperset(c1))

#Union de conjuntos
c1.union(c2)
print(c1==c4)
c1.update(c2)
c1={1,2,3}
c2={3,4,5}
c3={-1,99,8}
c4={1,2,3,4,5}
#Difference devuelve los elementos diferentes en los conjuntos
print(c1.difference(c2))
#Agrega los elementos diferentes del elemento pasado pro argumento en el conjunto a consultar
print(c1.difference_update(c2))

print(c1.intersection_update(c2))
#Diferencia simetrica
print(c1.symmetric_difference(c3))




