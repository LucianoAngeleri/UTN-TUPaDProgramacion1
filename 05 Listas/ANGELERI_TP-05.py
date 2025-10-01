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

# print("Ejercicio 3")

# import random

# cant_num_random =15
# lista_num_random =[]
# lista_num_pares =  []
# lista_num_impares =  []


# for num in range (cant_num_random):
#     numero_random = random.randint(1,100)
#     lista_num_random.append(numero_random)

# for num in lista_num_random:
#     if num % 2 == 0:
#         lista_num_pares.append(num)
#     else:
#         lista_num_impares.append(num)

# print(f"Números originales ({len(lista_num_random)} elementos):")
# for num_random in lista_num_random:
#     print(num_random, end=" ")
# print()

# print(f"Números pares ({len(lista_num_pares)} elementos):")
# for num_par in lista_num_pares:
#     print(num_par, end=" ")
# print()

# print(f"Números impares ({len(lista_num_impares)} elementos):")
# for num_impar in lista_num_impares:
#     print(num_impar, end=" ")

#-----------------------------------------------------------------------------------------------------------------

#4)Dada una lista con valores repetidos: 
# datos=[1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

# print("Ejercicio 4")

# datos=[1,3,5,3,7,1,9,5,3]
# datos_sin_repetir =[]

# for dato in datos:
#     if dato not in datos_sin_repetir:
#         datos_sin_repetir.append(dato)

# print("Lista original:")
# for dato in datos:
#     print(dato, end=" ")
# print()

# print("Lista sin datos repetidos:")
# for dato in datos_sin_repetir:
#     print(dato, end=" ")

#-----------------------------------------------------------------------------------------------------------------

#5)Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# print("Ejercicio N°5")

# estudiantes = ["Luciano", "Carlos", "María", "Juan", "Lucía", "Iván", "Sofía", "Diego"]

# print("Lista estudiantes presentes:")
# for estudiante in estudiantes:
#     print(estudiante, end=" ")

# print("Desea añadir un nuevo estudiante o eliminar uno existente?")
# while True:
#     op = input("Presione: (A)-Añadir o (E)-Eliminar: ").upper()
    
#     if op == "A" or op == "E":
#         break 
#     else:
#         print("Opción incorrecta. Por favor ingrese 'A' para añadir o 'E' para eliminar.")

# if op == "A":
#     nuevo_estudiante = str(input("Ingrese el nombre del nuevo estudiante: "))
#     estudiantes.append(nuevo_estudiante)
#     print(f"Se agregó a {nuevo_estudiante}")
# elif op == "E":
#     eliminar_estudiante = str(input("Ingrese el nombre del estudiante a eliminar: "))
#     if eliminar_estudiante in estudiantes:
#         estudiantes.remove(eliminar_estudiante)
#         print(f"Se eliminó a {eliminar_estudiante}")
#     else:
#       print(f"No se encontró a {eliminar_estudiante}")
# else:
#     print("Ingrese una opcion correcta")

# print("Lista estudiantes presentes(modificada):")
# for estudiante in estudiantes:
#     print(estudiante, end=" ")

#-----------------------------------------------------------------------------------------------------------------

#6)Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

# print("Ejercicio N°6")

# lista_num=[1,3,5,6,7,2,9]
# nueva_lista_num =[]

# print(f"Lista original: {lista_num}")

# ultimo_elemento = lista_num[-1]
# nueva_lista_num = [ultimo_elemento]

# for num in range(len(lista_num) - 1):
#     nueva_lista_num.append(lista_num[num])

# print("Lista rotada hacia la derecha:")
# for numero in nueva_lista_num:
#     print(numero, end=" ")

#-----------------------------------------------------------------------------------------------------------------

#7)Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica

# print("Ejercicio N°7")

# temperaturas =[ [15,21],
#                 [15,25],
#                 [15,28],
#                 [16,34],
#                 [19,35],
#                 [18,30],
#                 [14,21]]
# temp_max =0
# temp_min=100
# temp_max_suma=0
# temp_min_suma=0
# temp_max_promedio=0
# temp_min_promedio=0
# dia_amplitud=0
# amplitud_max=0
# dia_amplitud_max=0

# for dia in range(len(temperaturas)):

#     if temperaturas[dia][1] > temp_max:
#         temp_max = temperaturas[dia][1]

#     if temperaturas[dia][0] < temp_min:
#         temp_min = temperaturas[dia][0]

#     temp_max_suma += temperaturas[dia][1]
#     temp_min_suma += temperaturas[dia][0]

#     amplitud_dia= temperaturas[dia][1] - temperaturas[dia][0]

#     if amplitud_dia > amplitud_max:
#         amplitud_max = amplitud_dia
#         dia_amplitud_max = dia
#     print(f"Día {dia+1}")
#     print(f"Temp. Mínima: {temperaturas[dia][0]}°C")
#     print(f"Temp. Máxima: {temperaturas[dia][1]}°C")
#     print(f"Amplitud térmica: {amplitud_dia}°C")

# temp_max_promedio = temp_max_suma / len(temperaturas)
# temp_min_promedio = temp_min_suma / len(temperaturas)
# print(f"------------------------------------------------")
# print(f"Temperatura máxima promedio: {temp_max_promedio}°C")
# print(f"Temperatura mínima promedio: {temp_min_promedio}°C")
# print(f"Amplitud máxima registrada: {amplitud_max}°C en el día {dia_amplitud_max + 1}")

#-----------------------------------------------------------------------------------------------------------------

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

#-----------------------------------------------------------------------------------------------------------------

#9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

print("Ejercicio N°9")

tablero=[["-","-","-"],
         ["-","-","-"],
        ["-","-","-"]]
juego_terminado = False
turno = "X"
movimientos_realizados = 0
while juego_terminado != True:
    print("""
1 | 2 | 3 
==+===+===
 4 | 5 | 6 
==+===+===
7 | 8 | 9 
          """)

    posicion_valida = False

    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            celda = tablero[fila][columna]
            print(celda, end=" ")
            if columna < len(tablero[fila]) - 1:
                print("|", end=" ")
        print()
        if fila < len(tablero) - 1:
            print("==+===+===")

    while posicion_valida != True:
        
        jugador_posicion_str = input(f"Jugador ({turno}) - Ingrese la posición (1-9) donde desea colocar su marca: ")

        if jugador_posicion_str.isdigit():

            jugador_posicion = int(jugador_posicion_str)

            if jugador_posicion >= 1 and jugador_posicion <= 9:
                match jugador_posicion:
                    case 1:
                        if tablero[0][0] == "-":
                            tablero[0][0] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 2:
                        if tablero[0][1] == "-":
                            tablero[0][1] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue             
                    case 3:
                        if tablero[0][2] == "-":
                            tablero[0][2] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 4:
                        if tablero[1][0] == "-":
                            tablero[1][0] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 5:
                        if tablero[1][1] == "-":
                            tablero[1][1] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 6:
                        if tablero[1][2] == "-":
                            tablero[1][2] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 7:
                        if tablero[2][0] == "-":
                            tablero[2][0] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 8:
                        if tablero[2][1] == "-":
                            tablero[2][1] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue                
                    case 9:
                        if tablero[2][2] == "-":
                            tablero[2][2] = turno
                            break
                        else:
                            print("La posición ya está ocupada. Intente nuevamente.")
                            continue
                posicion_valida = True
            else:
                print("Posición inválida. Ingrese un número entre 1 y 9.")
        else:
            print("Entrada inválida. Por favor, ingrese un número .")

    movimientos_realizados += 1

    victoria = False

    marca = turno

    if (tablero[0][0] == marca and tablero[0][1] == marca and tablero[0][2] == marca):
        victoria = True
    elif (tablero[1][0] == marca and tablero[1][1] == marca and tablero[1][2] == marca):
        victoria = True
    elif (tablero[2][0] == marca and tablero[2][1] == marca and tablero[2][2] == marca) :
        victoria = True

    # B. ColuTnas
    elif (tablero[0][0] == marca and tablero[1][0] == marca and tablero[2][0] == marca) :
        victoria = True
    elif (tablero[0][1] == marca and tablero[1][1] == marca and tablero[2][1] == marca) :
        victoria = True
    elif (tablero[0][2] == marca and tablero[1][2] == marca and tablero[2][2] == marca) :
        victoria = True

    # C. Diagonales
    elif (tablero[0][0] == marca and tablero[1][1] == marca and tablero[2][2] == marca) : 
        victoria = True
    elif (tablero[0][2] == marca and tablero[1][1] == marca and tablero[2][0] == marca) : # 
        victoria = True

    if victoria:
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                celda = tablero[fila][columna]
                print(celda, end=" ")
                if columna < len(tablero[fila]) - 1:
                    print("|", end=" ")
            print()
            if fila < len(tablero) - 1:
                print("==+===+===")
        print(f"\nEl jugador {turno} ha ganado!")
        juego_terminado = True
        
    elif movimientos_realizados == 9:
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                celda = tablero[fila][columna]
                print(celda, end=" ")
                if columna < len(tablero[fila]) - 1:
                    print("|", end=" ")
            print()
            if fila < len(tablero) - 1:
                print("==+===+===")
        print("\n Es un Empate. El tablero está lleno.")
        juego_terminado = True
    
    else:
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
    
#-----------------------------------------------------------------------------------------------------------------

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.