# Crea un script que dada una tupla de números, devuelva la tupla con los numeros
# ordeandos en orden descendente.
print("----6----")

# Creamos tupla con numeros
tupla = (2,9,4,8,5,6,7,3,1)
# Creamos tupla con numeros ordenados
print(tupla)
tupla_ordenados = sorted(tupla)

# devolvemos la tupla con los numeros
# ordeandos en orden descendente.
tupla_ordenados.reverse()
print(tupla_ordenados)


# Crea un script que dada una tupla con números enteros repetidos, elimine los
# duplicados. (Puedes usar sets)
print("----7----")
# Creamos tupla con números enteros repetidos
tupla = (2,2,5,3,4,4,5,3,3,1,1,1,1,3,7,7,7)
print(tupla)

# Eliminamos duplicados
tupla_dup = set(tupla)
tupla_dup = tuple(tupla_dup)
print(tupla_dup)

# Crea un script que dada una tupla y un numero entero, devuelve verdadero si el
# numero se encuentra en la tupla y falso en el caso contrario.
print("----8----")
# Creamos variable con numero y tupla

tupla = (2,3,4,5,6,7,8)
numero = 5
print(tupla, "El numero es: ",numero)

for num in range(len(tupla)):
    if numero in tupla:
        print("Verdadero")
        break
    else:
        print("Falso")
        break
    
# O mas facil es:

comprobacion = numero in tupla
print(comprobacion)
        

# Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas

print("----9----")

# Creamos dos tuplas
tupla1 = (2,4,6)
tupla2 = (5,3,3)
print(tupla1)
print(tupla2)
# creamos tupla resultante
tupla_res = (tupla1 + tupla2)
print(tupla_res)

print("----10----")
#  Crea un script que dada una tupla de números devuelva e máximo y el mínimo

# creamos tupla

tupla = (7,3,2,1,65,33,12,31)
num_max = max(tupla)
num_min = min(tupla)
print("El maximo:", num_min)
print("El minimo:",num_max)



print("----11----")
# Crea un script que dada una tupla con strings devuelva el string más largo y el más
# corto. (Prueba añadiendo key=len a las funciones max y min).

# creamos tupla con strings 
tupla = ("Hola", "Bienvenida!", "Amargo")
# creamos script
string_largo = max(tupla, key=len)
string_corto = min(tupla, key=len)
print("El string mas largo:",string_largo)
print("El string mas corto:",string_corto)
# Luego haremos con script

print("----12----")

# Crea un script que dada una tupla devuelva el contenido en orden revertido.

# creamos tupla

tupla = (2,3,3,"Holaa",3,3,1,"Si!")
print(tupla)

# creamos script
tupla_revertida = tuple(reversed(tupla))

print(tupla_revertida)


print("----13----")

# Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos
# elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos
# elementos de la tupla interna correspondiente.

# Creamos tupla de tuplas

tupla1 = (2,4)
tupla2 = (5,3)
tupla3 = (6,7)

tupla_principal = (tupla1, tupla2, tupla3)
print(tupla_principal)

# creamos script
nueva_tupla = []



for i in range(len(tupla_principal)):
    suma = sum(tupla_principal[i])
    nueva_tupla.append(suma)

# imprimimos el resultado
print(nueva_tupla)

# convertimos class list en tuple
nueva_tupla1 = tuple(nueva_tupla)
print(type(nueva_tupla))
print(nueva_tupla1)
print(type(nueva_tupla1))

# o mas facil

mis_tuplas = tuple(sum(tuplas) for tuplas in tupla_principal)
print(mis_tuplas)

# Siguiente en ejercicio3!!!