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

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese segundo número entero: "))
suma = 0
if num1 < 0 or num2 < 0:
    print("Ingrese un número válido")
else:
    if num1 > num2:
        for contador in range(num2+1,num1):
            suma = suma + contador
    elif num1 < num2:
        for contador in range(num1+1,num2):
            suma = suma + contador
    print(f"La suma de los números comprendidos entre {num1} y {num2} es {suma}")

#-----------------------------------------------------------------------------------------------------------------

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#-----------------------------------------------------------------------------------------------------------------

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#-----------------------------------------------------------------------------------------------------------------

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

#-----------------------------------------------------------------------------------------------------------------

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

#-----------------------------------------------------------------------------------------------------------------

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#-----------------------------------------------------------------------------------------------------------------

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

#-----------------------------------------------------------------------------------------------------------------

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.