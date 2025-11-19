#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# print("Ejercicio 1")

# def imprimir_hola_mundo():
#     print("Hola Mundo!")
# imprimir_hola_mundo()


#2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# print("Ejercicio 2")

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}! Cómo estas?")
# nombre_usuario = input("Ingrese su nombre: ")
# saludar_usuario(nombre_usuario)

#3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# print("Ejercicio 3")

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# nombre_usuario = input("Ingrese su nombre: ")
# apellido_usuario = input("Ingrese su apellido: ")
# edad_usuario = input("Ingrese su edad: ")
# residencia_usuario = input("Ingrese su residencia: ")

# informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# print("Ejercicio 4")
# from math import pi

# def calcular_area_circulo(radio):
#     return pi* radio*radio 

# def calcular_perimetro_circulo(radio):
#     return 2* pi * radio

# radio_circulo = float(input("Ingrese el radio del circulo: "))

# print(f"El área de un circulo de {radio_circulo} es {calcular_area_circulo(radio_circulo)}")
# print(f"El perímetro de un circulo de {radio_circulo} es {calcular_perimetro_circulo(radio_circulo)}")

#5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# print("Ejercicio 5")

# def segundos_a_horas(segundos):
#     return segundos / 3600

# segundos_usuario=int(input("Ingrese los segundos: "))
# print(f"{segundos_usuario} segundos son: {segundos_a_horas(segundos_usuario)} horas")

#6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# print("Ejercicio 6")

# def tabla_multiplicar(numero):
#     for i in range (0,11):
#         print(f"{numero} x {i} = {numero*i}")
# num = int(input("Ingrese un número para obtener su tabla de multiplicar: "))
# tabla_multiplicar(num)

#7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# print("Ejercicio 7")

# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = (a / b) if b != 0 else "No se puede dividir por 0."

#     opreaciones = ("Suma", suma,"Resta", resta,"Multiplicacion", multiplicacion,"Division", division)
#     return opreaciones
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# resultados = operaciones_basicas(num1, num2)

# print(f"Operaciones entre {num1} y {num2}:")
# print(f"  Suma:           {num1} + {num2} = {resultados[1]}")
# print(f"  Resta:          {num1} - {num2} = {resultados[3]}")
# print(f"  Multiplicación: {num1} × {num2} = {resultados[5]}")
# print(f"  División:       {num1} ÷ {num2} = {resultados[7]}")


#8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# print("Ejercicio 8")

# def calcular_imc(peso, altura):
#     imc = peso / (altura ** 2)
#     return imc
# peso_usuario = float(input("Ingrese su peso en kilogramos: "))
# altura_usuario = float(input("Ingrese su altura en metros: "))

# imc_usuario = calcular_imc(peso_usuario,altura_usuario)
# print(f"El IMC del usuario que pesa {peso_usuario}kg y mide {altura_usuario}m es: {imc_usuario:.2f}")

#9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# print("Ejercicio 9")

# def celsius_a_fahrenheit(celsius):
#     return (celsius*9/5)+32

# celsius = float(input("Ingrese la temperatura en Celsius: "))
# fahrenheit = celsius_a_fahrenheit(celsius)
# print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

print("Ejercicio 10")

def calcular_promedio(a, b, c):
    return (a+b+c)/3

print("Se va a calcular el promedio de 3 numeros ingresado")
num1 = float(input("Ingrese el primer número:"))
num2 = float(input("Ingrese el segundo número:"))
num3 = float(input("Ingrese el tercer número:"))

promedio = calcular_promedio(num1,num2,num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
