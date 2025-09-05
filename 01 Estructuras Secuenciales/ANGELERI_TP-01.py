""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. """
mensaje = "Hola Mundo!"
print(mensaje)

""""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
"""
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")

""""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""
nombre = input("Ingrese su nombre: ")
apellido =  input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar = input("Ingrese su lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

""""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro
"""
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
area = pi * radio * radio  
perimetro = 2 * pi * radio

print(f"El area de un círculo de radio = {radio} es {area}")
print(f"El perímetro de un círculo de radio = {radio} es {perimetro}")

""""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos son {horas} horas")

""""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""
numero = int(input("Ingrese un número para ver su tabla de multiplicación: "))

print(f"{numero} x 0 = {numero * 0}")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

""""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""
num1 = int(input("Ingrese el primer número entrero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entrero distinto de 0: "))

suma = num1 + num2
division = num1 / num2
producto = num1 * num2
resta = num1 - num2

print(f"Suma: {num1} + {num2} = {suma}")
print(f"División: {num1} / {num2} = {division}")
print(f"Multiplicación: {num1} * {num2} = {producto}")
print(f"Resta: {num1} - {num2} = {resta}")

""""
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
IMC = peso en kg / (altura en m)^2
"""
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura* altura)

print(f"Su IMC es: {imc}")

""""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
Temperatura en Fahrenheit = ((9/5)*Temperatura en Celsius) + 32
"""
temp_cels = float(input("Ingrese la temperatura en grados Celsius: "))

temp_far = ((9/5)* temp_cels) + 32

print(f"{temp_cels}°C es igual a {temp_far}°F")

""""
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print("Ahora calcularemos el promedio de esos numeros.")
promedio = (num1 + num2 + num3)/3

print(f"El promedio de {num1}, {num2} y {num3} es {promedio}")
