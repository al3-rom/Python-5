"""
DATOS CLIENTES:
Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
segunda base de datos contiene el nombre del cliente, la dirección y el historial de
pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre.


Pista: Tus datos de entrada podrían ser así —>
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria",
"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", “555-9012")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]),
("Luis", "Calle 789", ["Libro4"])] 

"""
# Creamos la lista con base de datos
base_datos1 = [
    ("Alejandro", "sasha.stankevich223@gmail.com", +34606761598),
    ("Alvaro", "Els masos", +34834617386),
    ("Alex", "La canonja", +34912331393)
    ]
base_datos2 = [
    ("Alvaro", "Els masos", ["Isaac1", "Pelota bascket"]),
    ("Alex", "La canonja", ["Guantes de boxeo", "Google pixel 8"]),
    ("David", "El vendrell", ["Mario Party", "Altavoz"]),
    ]
# Cambiamos de list a tuple

base_datos1 = tuple(base_datos1)
base_datos2 = tuple(base_datos2)
# Tomamos bases de datos
nueva_lista = []
nueva_lista1 = []

# Añadimos a nueva lista solo nombres
for cliente in base_datos1:
    nueva_lista.append(cliente[0])

# Añadimos a nueva lista solo nombres
for cliente in base_datos2:
    nueva_lista1.append(cliente[0])

# Cambiamos de tuple a set para utilizar funcion (intersection)
nueva_lista1 = set(nueva_lista1)
nueva_lista = set(nueva_lista)
# Imprimimos los nombres de ambas bases
print("Clientes de primera base",nueva_lista)
print("Clientes de segunda base",nueva_lista1)
print(".....")
# Añadimos a nueva lista solo nombres de ambas
clientes_en_ambas = nueva_lista.intersection(nueva_lista1)
# imprimimos los nombres
print(clientes_en_ambas)
print(type(clientes_en_ambas))
print(".....")
# Cambiamos a tuple
clientes_en_ambas = tuple(clientes_en_ambas)

# Imprimimos el resultado
print("Los clientes que aparecen en ambas bases de datos son:", clientes_en_ambas)
print(type(clientes_en_ambas))