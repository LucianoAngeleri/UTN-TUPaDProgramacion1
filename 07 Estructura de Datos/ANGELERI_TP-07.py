#1)  Dado el diccionario precios_frutas
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
"""
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

print("Ejercicio 1")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

print("Ejercicio 2")

precios_frutas.update({
    "Banana" : 1330,
    "Manzana" : 1700,
    "Melón" : 2800
})

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print("Ejercicio 3")

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#4)  Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
"""
contactos = {"Juan": "123456", "Ana": "987654"}
#Consultar: "Juan" -> muestra "123456"
"""

print("Ejercicio 4")

contactos ={}
for i in range(0,2):
    nombre_ingresado = str(input(f"{i+1}. Ingrese un nombre de contacto: "))
    numero_ingresado = str(input(f"{i+1}. Ingrese un número de contacto: "))
    contactos.update({
        nombre_ingresado: numero_ingresado}
    )
print("Contactos agregados correctamente.")

nombre_consulta = str(input("Ingresa un nombre de contacto para consultar: "))

if nombre_consulta in contactos:
    numero_consulta = contactos[nombre_consulta]
    print(f"El número de {nombre_consulta} es: {numero_consulta}")
else:
    print(f"Error: El contacto '{nombre_consulta}' no se encuentra en la agenda.")

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

print("Ejercicio 5")
from typing import Counter

frase = str(input("Ingrese una frase: "))

palabras = frase.lower().split()
palabras_unicas = set(palabras)

recuento_diccionario = dict(Counter(palabras))

print("Salida:")
print(f"Palabras_únicas: {palabras_unicas}")
print(f"Recuento: {recuento_diccionario}")

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

print("Ejercicio 7")

aprobados_parcial1 = {101, 105, 110, 115, 120, 125, 130}
aprobados_parcial2 = {105, 115, 120, 135, 140, 145}

print(f"Aprobados Parcial 1: {aprobados_parcial1}")
print(f"Aprobados Parcial 2: {aprobados_parcial2}")

aprobados_ambos = aprobados_parcial1 & aprobados_parcial2
print("Estudiantes que aprobaron AMBOS parciales:")
print(aprobados_ambos)

solo_un_parcial = aprobados_parcial1 ^ aprobados_parcial2
print("Estudiantes que aprobaron SOLO UNO de los dos: ")
print(solo_un_parcial)

total_aprobados = aprobados_parcial1 | aprobados_parcial2
print("Lista TOTAL de estudiantes que aprobaron AL MENOS un parcial:")
print(total_aprobados)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

print("Ejercicio 8")

productos = {
    "Martillo": 50,
    "Tornillo": 200,
    "Clavo": 150
}

while True:
    print("--- Opciones ---")
    print("1. Consultar stock")
    print("2. Agregar/Actualizar stock o producto")
    print("3. Salir")
    opcion = str(input("Seleccione una opción (1-3): "))

    match opcion:
        case "1":
            nombre_producto = input("Ingrese el producto a consultar: ")
            if nombre_producto in productos:
                stock = productos[nombre_producto]
                print(f"El stock actual de '{nombre_producto}' es: {stock} unidades.")
            else:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
        case "2":
            nombre_producto = input("Ingrese el nombre del producto a agregar/actualizar: ")
            cantidad = int(input(f"Ingrese la cantidad de unidades a agregar: "))
            
            if nombre_producto in productos:              
                productos[nombre_producto] += cantidad
                print(f"Stock de '{nombre_producto}' actualizado. Nuevo stock: {productos[nombre_producto]}.")
            else:
                print("El producto ingresado no existe, se añadirá un nuevo producto.")
                productos[nombre_producto] = cantidad
                print(f"Nuevo producto '{nombre_producto}' agregado con stock inicial de {cantidad}.")

            print(f"Inventario actualizado: {productos}")
        case "3":
            print("Saliendo del sistema de inventario.")
            break
        case _:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.Ejemplo:
"""
agenda = {
    ("lunes","10:00"): "Reunión",
    ("martes","15:00"): "Clase de ingles",
}
"""
# Permití consultar qué actividad hay en cierto día y hora.

print("Ejercicio 9")

agenda = {
    ("lunes", "10:00"): "Reunión con compañeros",
    ("martes", "15:00"): "Clase de ingles",
    ("miércoles", "09:00"): "Entrega de proyecto",
    ("lunes", "14:00"): "Llamada con cliente"
}

print("Agenda completa")
for clave_tupla, evento in agenda.items():
    dia, hora = clave_tupla
    print(f"Día: {dia} a las {hora}, {evento}")

dia_consulta = input("Ingrese el día a consultar (ej: lunes): ").lower()
hora_consulta = input("Ingrese la hora a consultar (ej: 10:00): ")

clave_busqueda = (dia_consulta, hora_consulta)
if clave_busqueda in agenda:
    evento = agenda[clave_busqueda]
    print(f"La actividad programada para el {dia_consulta} a las {hora_consulta} es: {evento}.")
else:
    print(f"No hay ninguna actividad programada para el {dia_consulta} a las {hora_consulta}.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
"""
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
"""

print("Ejercicio 10")

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "Brasil": "Brasilia"
}
print("Diccionario de paises y capitales original: ")
print(original)

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario invertido (Capital: País): ")
print(invertido)
