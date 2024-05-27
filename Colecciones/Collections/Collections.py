from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple


l=[1,2,3,4,1,2,3,1]
print(Counter(l))

animales = "gato perro canario perro canario perro"


print(Counter(animales))
animales.split()

#most comon muestra el elemento que mas se
# repite pasandole cantidad por argumento
# devuelve los que queremos ejemplo 1 devielve un unico valor.etc
c= Counter(animales.split())
print(c.most_common(1))
print(c)

l=[1,2,4,6,75,3,3,245,64,2,30.40,60]
c= Counter(l)
print(c.items())
list(c)

print(c)
c.items()
c.values()
sum(c.values())
