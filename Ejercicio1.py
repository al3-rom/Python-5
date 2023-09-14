# Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea.
print("----1----")
Tupla1 = (3,2,1)
print(Tupla1)
print(Tupla1[0])
print(Tupla1[1])
print(Tupla1[2])
print(type(Tupla1))

print("----2----")

# Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla.
# ¿Cuáles son las diferencias?

# Creamos una lista 
Lista = [3,2,1]
print(Lista)
Lista[0] = 1
print(Lista)
print(type(Lista))

# Ahora hacemos lo mismo con la tupla

Tupla2 = (3,2,1)
print(Tupla2)
# Tupla2[0] = 1
# print(Tupla2) No se puede, las tuplas no se modifican
print(type(Tupla2))

print("----3----")
 
# Crea una tupla de enteros y devuelve la suma de los elementos

Tupla3 = (3,2,1)
print(Tupla3)
print(sum(Tupla3))
print(type(Tupla3))

# Crea un script que dada una tupla que contiene strings cree una nueva tupla con el
# primer caracter de cada string.

print("----4----")

Tupla4 = ("Hola", "Ostras", "Like", "Amor",)
# Creamos una lista
letra = []
# Hacemos el script 
for i in range(len(Tupla4)):
        # Añadimos a una lista (letra) el primer caracter de cada string
        letra.append(Tupla4[i][0])
# Imprimimos por pantalla
print(letra)
print(type(letra))
letra = tuple(letra)
print(letra)
print(type(letra))

# Crea un script que dada una tupla de números devuelva el producto de todos los números pares. 

print("----5----")

# Creamos una tupla de números
Tupla5 = (8,4,3,3,5,6,2)
# Creamos una lista para guardar todos los números pares
pares = []
# Hacemos el bucle
for i in range(len(Tupla5)):
        if Tupla5[i] % 2 == 0:
                pares.append(Tupla5[i])
# Imprimimos por pantalla
print(pares)

# Siguiente parte en Ejercicio2!!!