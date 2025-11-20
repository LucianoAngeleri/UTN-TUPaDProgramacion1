#1)  Dado el diccionario precios_frutas
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
"""
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# print("Ejercicio 1")

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# precios_frutas["Naranja"]= 1200
# precios_frutas["Manzana"]= 1500
# precios_frutas["Pera"]= 2300

# print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# print("Ejercicio 2")

# precios_frutas.update({
#     "Banana" : 1330,
#     "Manzana" : 1700,
#     "Melón" : 2800
# })

# print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# print("Ejercicio 3")

# lista_frutas = list(precios_frutas.keys())

# print(lista_frutas)

#4)  Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
"""
contactos = {"Juan": "123456", "Ana": "987654"}
#Consultar: "Juan" -> muestra "123456"
"""

# print("Ejercicio 4")

# contactos ={}
# for i in range(0,2):
#     nombre_ingresado = str(input(f"{i+1}. Ingrese un nombre de contacto: "))
#     numero_ingresado = str(input(f"{i+1}. Ingrese un número de contacto: "))
#     contactos.update({
#         nombre_ingresado: numero_ingresado}
#     )
# print("Contactos agregados correctamente.")

# nombre_consulta = str(input("Ingresa un nombre de contacto para consultar: "))

# if nombre_consulta in contactos:
#     numero_consulta = contactos[nombre_consulta]
#     print(f"El número de {nombre_consulta} es: {numero_consulta}")
# else:
#     print(f"Error: El contacto '{nombre_consulta}' no se encuentra en la agenda.")

#5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
"""
#Entrada -> "hola mundo hola"
#Salida:
Palabras_únicas: {'hola', 'mundo'}
Recuento: {'hola': 2, 'mundo': 1}
"""

# print("Ejercicio 5")
# from typing import Counter

# frase = str(input("Ingrese una frase: "))

# palabras = frase.lower().split()
# palabras_unicas = set(palabras)

# recuento_diccionario = dict(Counter(palabras))

# print("Salida:")
# print(f"Palabras_únicas: {palabras_unicas}")
# print(f"Recuento: {recuento_diccionario}")

#6)  Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. Ejemplo
"""
alumnos ={
    "Sofia": (10,9,8),
    "Luis": (6,7,7)
}
"""

print("Ejercicio 6")

alumnos ={}

num_alumnos = 3
num_notas = 3

for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    notas = []

    print(f"Ingrese las {num_notas} notas para {nombre}:")
    for j in range(num_notas):
        nota = float(input(f"Ingrese la nota n° {j+1}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("Listado de Alumnos:")
print(alumnos)

print("--- Promedio de cada alumno ---")

for nombre_alumno, notas_tupla in alumnos.items():   
    promedio =sum(notas_tupla) / len(notas_tupla)
    
    print(f"El promedio de {nombre_alumno} es: {promedio:.2f}")

#7)  Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


#print("Ejercicio 7")

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

#print("Ejercicio 8")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.Ejemplo:
"""
agenda = {
    ("lunes","10:00"): "Reunión",
    ("martes","15:00"): "Clase de ingles",
}
"""
# Permití consultar qué actividad hay en cierto día y hora.

#print("Ejercicio 9")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
"""
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
"""

#print("Ejercicio 10")
