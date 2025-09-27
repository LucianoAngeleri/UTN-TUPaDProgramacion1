#1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# print("Ejercicio 1")

# notas =[8.5, 7.0, 9.2, 6.5, 8.0, 7.5, 9.0, 5.5, 8.8, 7.2]

# suma_notas = 0
# nota_max=0.0
# nota_min=100.0

# print("Lista de notas:")
# for nota in range(len(notas)):
#     print(f"Estudiante({nota+1}): {notas[nota]}")
#     suma_notas += notas[nota]
#     if notas[nota] > nota_max:
#         nota_max = notas[nota]
#     if notas[nota] < nota_min:
#         nota_min=notas[nota]
 
# print("El promedio de notas es: ", suma_notas/len(notas))
# print("La nota máxima es:", nota_max)
# print("La nota mínima es:", nota_min) 

#-----------------------------------------------------------------------------------------------------------------

#2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# print("Ejercicio 2")

# print("Ejercicio 2")
# lista_productos =["","","","",""]
# lista_productos_ordenados = []
# producto_eliminar = ""

# for producto in range(len(lista_productos)):
#     lista_productos[producto] = str(input(f"{producto+1} - Ingrese el nombre de un producto:"))

# lista_productos_ordenados = sorted(lista_productos)

# print("Lista de productos original:")
# for producto in range(len(lista_productos)):
#     print(f"Producto({producto+1}): {lista_productos[producto]}")
# print("Lista de productos ordenados alfabeticamente:")
# for producto in range(len(lista_productos_ordenados)):
#     print(f"Producto({producto+1}): {lista_productos_ordenados[producto]}")

# producto_eliminar= str(input("Qué producto desea eliminar? Ingrese el nombre del producto: "))
# if producto_eliminar in lista_productos:
#   lista_productos.remove(producto_eliminar)
#   print(f"El producto {producto_eliminar} ha sido eliminado correctamente")
#   print("Lista actualizada:", lista_productos)
# else:
#   print(f"El producto '{producto_eliminar}' no se encontró en la lista")

#-----------------------------------------------------------------------------------------------------------------

#3)Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista

import random

cant_num_random =15
lista_num_random =[]
lista_num_pares =  []
lista_num_impares =  []


for num in range (cant_num_random):
    numero_random = random.randint(1,100)
    lista_num_random.append(numero_random)

for num in lista_num_random:
    if num % 2 == 0:
        lista_num_pares.append(num)
    else:
        lista_num_impares.append(num)

print(f"Números originales ({len(lista_num_random)} elementos):")
for num_random in lista_num_random:
    print(num_random, end=" ")
print()

print(f"Números pares ({len(lista_num_pares)} elementos):")
for num_par in lista_num_pares:
    print(num_par, end=" ")
print()

print(f"Números impares ({len(lista_num_impares)} elementos):")
for num_impar in lista_num_impares:
    print(num_impar, end=" ")


#-----------------------------------------------------------------------------------------------------------------

#4)Dada una lista con valores repetidos: 
# datos=[1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

#-----------------------------------------------------------------------------------------------------------------

#5)Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

#-----------------------------------------------------------------------------------------------------------------

#6)Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

#-----------------------------------------------------------------------------------------------------------------

#7)Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica

#-----------------------------------------------------------------------------------------------------------------

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

#-----------------------------------------------------------------------------------------------------------------

#9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
 

#-----------------------------------------------------------------------------------------------------------------

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.