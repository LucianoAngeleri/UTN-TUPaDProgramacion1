# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

print("Ejercicio 1")

def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num-1)
    
numero_ingresado = int(input("Ingrese el número para calcular su factorial: "))
for i in range(1, numero_ingresado + 1):
    print(f"El factorial de {i} es: {factorial_recursivo(i)}")