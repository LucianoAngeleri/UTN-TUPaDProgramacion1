# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad:"))

# if edad > 18:
#     print("Es mayor de edad")

#-----------------------------------------------------------------------------------------------------------------

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar elmensaje “Desaprobado”

# nota = float(input("Ingrese su nota:"))

# if nota >=6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

#-----------------------------------------------------------------------------------------------------------------

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Ingrese un número:"))

# if numero % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")    

#-----------------------------------------------------------------------------------------------------------------

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad:"))

# if edad < 12:
#     print("Es Niño/a")
# elif edad < 18:
#     print("Es Adolescente")
# elif edad < 30:
#     print("Es  Adulto/a joven")
# else:
#     print("Es Adulto/a")

#-----------------------------------------------------------------------------------------------------------------

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# password = input("Ingrese su contraseña, debe contener entre 8 y 14 caracteres:")

# if len(password) >= 8 and len(password) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#-----------------------------------------------------------------------------------------------------------------

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
#from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
#mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# mediana= median(numeros_aleatorios)
# moda= mode(numeros_aleatorios)
# media= mean(numeros_aleatorios)

# print(f"Números:{numeros_aleatorios}")
# print("----------------------------------")
# print(f"Mediana:{mediana}")
# print(f"Moda:{moda}")
# print(f"Media:{media}")

# if (media > mediana) and (mediana > moda):
#     print("Hay sesgo positivo o a la derecha")
# elif (media < mediana) and (mediana < moda):
#     print("Hay sesgo negativo o a la izquierda")
# elif media == mediana == moda:
#     print("Sin sesgo")
# else:
#     print("No se encontró un tipo de sesgo identificable")

#-----------------------------------------------------------------------------------------------------------------

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# frase = str(input("Ingrese una frase o palabra:"))

# ultimo_caracter= frase[-1].lower() 

# # con frase[-1] obtenemos el ultimo caracter de la y utilizamos el metodo .lower() para pasar la cadena a minúsculas a fin de comparar correctamente en el if

# if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u":
#     print(frase+"!")
# else:
#     print(frase)

#-----------------------------------------------------------------------------------------------------------------

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingrese su nombre:"))

print("""Elija una de las siguientes opciones
=======================================================
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.""")

opcion = int(input("Ingrese la opcion:"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingrese una opcion válida.")
