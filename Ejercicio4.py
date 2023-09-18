"""
RED SOCIAL:
Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro",
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])]
Pista 2: Para eliminar duplicidades puedes usar sets 

"""
base_de_datos = (("Alex", ["Alvaro","Mario","Alejandro", "Alvaro", "Laura"]),
                 ("Alejandro", ["Alex", "Mario", "Alvaro", "Ruge", "Alvaro"]), 
                 ("Alvaro", ["Alex", "Laura", "Sashka", "Alex"]))

tupla_nueva = []

for tupla in base_de_datos:
    tupla_nueva.append(tupla[0])
    tupla_nueva.append(set(tupla[1]))

print(tupla_nueva)

# No se que hacer
