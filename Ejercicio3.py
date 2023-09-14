# Crea un set y elimina uno de sus elementos.

print("----14----")

# Creamos un set
set1 = {2,3,4}
print(set1)

# Eleminamos uno de sus elementos
set1.discard(2)
print(set1)

# Crea un set vacío.
print("----15----")
# Creamos set vacio

set_vacio = set()
print(set_vacio)
print(type(set_vacio))


print("----16----")
# Crea dos sets y encuentra su union, su intersección y su diferencia.

# Creamos sets
set1 = {2,3,4,5}
set2 = {4,3,2,1}
print(set1)
print(set2)
# Encontramos su union, su intersección y su diferencia.
union = set1.union(set2)
interseccion = set1.intersection(set2)
diferencia1 = set1.difference(set2)
diferencia2 = set2.difference(set1)
# Imprimimos resultado
print("Union:", union)
print("Intersección:", interseccion)
print("Diferencia1:", diferencia1)
print("Diferencia2:", diferencia2)

print("----17----")
# Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos
# comunes de ambos.

# Creamos sets

set1 = {2,3,4,5,9}
set2 = {2,3,5,7,8}
print(set1)
print(set2)

print("....")
# Creamos script

set_nuevo = {}
set_nuevo = set1.intersection(set2)
print(set_nuevo)
print(type(set_nuevo))

print("----18----")
# Crea un script que dado un set con números devuelva el numero máximo y mínimo

# Creamos set 

set1 = {3,2,1,5,22,65}
print(set1)
print("Numero maximo es:", max(set1), "y numero minimo es:", min(set1))

# Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de
# cada uno de los sets.

print("----19----")

# Creamos sets

set1 = {2,3,4,5,9,5,5,1}
set2 = {2,3,5,7,8,7,7,1}
print(set1)
print(set2)
# Creamos script
set_nuevo = set1.union(set2)
print("....")
print(set_nuevo)

print("----20----")
# Crea un set con colores y comprueba si cierto color se encuentra en el set.

# Creamos set
setColores = {"verde", "amarillo", "rojo", "negro"}
print(setColores)
# Comprobamos si el color que necesitamos se encuentra en el set

nuestro_color = "amarillo"
print(nuestro_color)
if nuestro_color in setColores:
    print("Nuestro color esta en el set")
else:
    print("Nuestro color no esta")


print("----21----")
# Crea un script que dados dos sets cree un nuevo set con los elementos que están en
# el primer set pero no en el segundo.

set1 = {2,3,4,5,6}
set2 = {3,5,1,6,2}
print(set1, set2)
print("....")

nuevo_set = set1
print(nuevo_set)
print(type(nuevo_set))


print("----22----")
# Crea un script que dado un set de enteros devuelva el producto de todos los números
# dentro del set.



