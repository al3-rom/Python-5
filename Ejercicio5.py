"""
LA BIBLIOTECA:
Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
libro y el apellido del autor.
Pista: Tus datos de entrada podrían ser así —> lista_libros = [(^El aleph', ^Jorge Luis
Borges'), ('Cien años de soledad', ^Garbriel Garcia Márquez'), ('La ciudad y los perros',
^Mario Vargas Llosa')] 

"""

lista_libros = [
    ("Ben10", "Alejandro Romero Stankevich"),
    ("IsAAc", "Alvaro Stricly Hiphop"),
    ("Boxeo", "Mario Polaco Español")
]
# lista_libros = tuple(lista_libros)
# print(type(lista_libros))

# nueva_tupla = []

# for tupla in lista_libros:
  #  nueva_tupla.append(tupla[0])
   # nueva_tupla.append(tupla[1])
#print(nueva_tupla)

#nuevo = nueva_tupla[1][1]
#print(nuevo)

titulos_y_apellidos = []
for tupla in lista_libros:
    titulo, autor = tupla
    apellido = autor.split()[-1]
    print(apellido)

    titulos_y_apellidos.append((titulo,apellido))
print(titulos_y_apellidos)