#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

# print("Ejercicio 1")

# def factorial_recursivo(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial_recursivo(num-1)
    
# numero_ingresado = int(input("Ingrese el número para calcular su factorial: "))
# for i in range(1, numero_ingresado + 1):
#     print(f"El factorial de {i} es: {factorial_recursivo(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# print("Ejercicio 2")

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)

# numero_ingresado = int(input("Ingrese el número para calcular ver la serie de Fibonacci hasta esta posición: "))
# print("Serie de Fibonacci:")
# for i in range(numero_ingresado + 1):
#     print(f"Posición:{i} = {fibonacci(i)}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.

# print("Ejercicio 3")

# def potencia_recursiva(n, m):
#     if m == 0:
#         return 1
#     else:
#         return n * potencia_recursiva(n, m - 1)

# print(potencia_recursiva(2, 3))

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

def a_binario(num):
    if num < 2:
        return str(num)
    else:
        return a_binario(num // 2) + str(num % 2)

numero_decimal = int(input("Ingrese un número entero positivo en base decimal: "))
print(f"El número {numero_decimal}, en Binario es: {a_binario(numero_decimal)}")