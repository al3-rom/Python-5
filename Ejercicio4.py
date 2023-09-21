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

# Datos de entrada
red_social = (("Alex", ["Alvaro","Mario","Alejandro", "Alvaro", "Laura", "Roger"]),
                 ("Alejandro", ["Alex", "Mario", "Alvaro", "Ruge", "Alvaro"]), 
                 ("Alvaro", ["Alex", "Laura", "Sashka", "Alex"]))

# Eliminar las cuentas duplicadas en amigos
red_social_sin_duplicados = []
for i in range(len(red_social)):
    # usuario = red_social[i][0]
    # amigos = red_social[i][1]
    usuario, amigos = red_social[i]
    amigos_sin_duplicados = list(set(amigos))
    red_social_sin_duplicados.append((usuario,amigos_sin_duplicados))

# Contar el numero de amigos de cada usuario
amigos_por_usuario = []
for usuario,amigos in red_social_sin_duplicados:
    amigos_por_usuario.append((usuario,len(amigos)))

amigos_por_usuario = tuple(amigos_por_usuario)
print(amigos_por_usuario)

# Obtener el usuario con mas amigos
lista_usuarios = [tupla[0] for tupla in amigos_por_usuario]
numero_amigos = [amigos[1] for amigos in amigos_por_usuario]

print(lista_usuarios)
print(numero_amigos)

indice_con_mas_amigos = numero_amigos.index(max(numero_amigos))

usuario_con_mas_amigos = lista_usuarios[indice_con_mas_amigos]
print(usuario_con_mas_amigos)
# Output: tuplas de tuplas -- usuario, numero de amigos
# Output: usuario con mas amigos
