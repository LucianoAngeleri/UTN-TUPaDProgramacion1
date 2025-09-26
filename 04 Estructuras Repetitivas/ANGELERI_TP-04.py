# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for contador in range(0,101):
#     print(contador)

#-----------------------------------------------------------------------------------------------------------------

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
# num = int(input("Ingrese un número entero para determinar la cantidad de dígitos: "))
# cant_digitos = 0
# digito = num

# if num == 0:
#     cant_digitos = 1
# elif num > 0:
#     while digito > 0:
#         digito = digito // 10
#         cant_digitos +=1

# if num >= 0:
#     print(f"El número {num} tiene {cant_digitos} dígitos")
# else:
#     print("Ingrese un número entero válido")

#-----------------------------------------------------------------------------------------------------------------

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese el primer número entero: "))
# num2 = int(input("Ingrese segundo número entero: "))
# suma = 0
# if num1 < 0 or num2 < 0:
#     print("Ingrese un número válido")
# else:
#     if num1 > num2:
#         for contador in range(num2+1,num1):
#             suma = suma + contador
#     elif num1 < num2:
#         for contador in range(num1+1,num2):
#             suma = suma + contador
#     print(f"La suma de los números comprendidos entre {num1} y {num2} es {suma}")

#-----------------------------------------------------------------------------------------------------------------

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# numero = int(input("Ingrese un número para sumar en secuencia o ingrese 0 para detener la suma: "))
# suma=0
# while numero != 0:
#     suma = suma + numero
#     numero=int(input("Ingrese un número para sumar en secuencia o ingrese 0 para detener la suma: "))
# print("La suma se detuvo.")
# print(f"La suma total es: {suma}")

#-----------------------------------------------------------------------------------------------------------------

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
# import random

# num_aleatorio = random.randint(0, 9)
# num_adivinado = False
# intentos=0

# print("Debes adivinar un número entre 0 y 9 para ganar")

# while not num_adivinado:
#     intentos +=1
#     num_valido = False

#     while not num_valido:
#         num_usuario= int(input("Ingrese un número entre 0 y 9: "))
#         if 0 <= num_usuario <= 9:
#             num_valido = True
#         else:
#             print("Número no válido.") 
   
#     if  num_usuario == num_aleatorio:
#         num_adivinado = True 
#     else:
#         print("Te equivocaste de número")

# print(f"Ganaste, adivinaste el numero en {intentos} intento/s")

#-----------------------------------------------------------------------------------------------------------------

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# for num in range(100,-1,-1):
#     if num % 2 == 0:
#         print(num)

#-----------------------------------------------------------------------------------------------------------------

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
# num_valido=False
# suma=0
# while not num_valido:
#     num_positivo = int(input("Ingrese un número positivo: "))
#     if num_positivo > 0:
#         num_valido= True
#         for i in range(0,num_positivo+1):
#             suma = suma + i
#     else:
#         print("Número Inválido.Ingrese un número positivo")
# print(f"La suma entre los números comprendido desde 0 hasta {num_positivo} es {suma}")

#-----------------------------------------------------------------------------------------------------------------

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
limite=100

cant_num_par=0
cant_num_impar=0
cant_num_positivo=0
cant_num_negativo=0
cant_ceros=0

for i in range (1,limite+1):
    num = int(input(f"{i}- Ingrese un número entero: "))
    if num % 2 ==0:
      cant_num_par +=1
    else:
      cant_num_impar +=1
    if num > 0:
        cant_num_positivo += 1
    elif num < 0:
        cant_num_negativo += 1
    else:
       cant_ceros += 1

print(f"Cantidad de números pares ingresados: {cant_num_par}")
print(f"Cantidad de números impares ingresados: {cant_num_impar}")
print(f"Cantidad de números positivos ingresados: {cant_num_positivo}")
print(f"Cantidad de números negativos ingresados: {cant_num_negativo}")
print(f"Cantidad de ceros: {cant_ceros}")

#-----------------------------------------------------------------------------------------------------------------

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

#-----------------------------------------------------------------------------------------------------------------

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.