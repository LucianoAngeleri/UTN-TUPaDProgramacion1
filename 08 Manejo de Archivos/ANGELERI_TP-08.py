# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre, precio,cantidad

with open("productos.txt", "w", encoding="utf8") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    archivo.write("Teclado,150,10\n")
    archivo.write("Notebook,1500,5\n")
    archivo.write("Auriculares,200,12\n")
    print("1. Catálogo de productos creado con éxito.")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r", encoding="utf8") as archivo:
    lineas = archivo.readlines()
    print("---- 2. Catálogo de productos ----")
    for linea in lineas[1:]:
        datos_producto = linea.strip().split(",")
        nombre = datos_producto[0]
        precio = datos_producto[1]
        cantidad = datos_producto[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt", "a", encoding="utf8") as archivo:
    print("---- 3. Agregar un nuevo producto por teclado ---- ")
    nombre_producto = input("Ingrese el nombre del producto: ").strip()
    precio_producto = input("Ingrese el precio del producto: ").strip()
    cantidad_producto = input("Ingrese la cantidad del producto: ").strip()
    archivo.write(f"{nombre_producto},{precio_producto},{cantidad_producto}\n")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

productos=[]

with open("productos.txt", "r", encoding="utf8") as archivo:
    print("---- 4. Cargar el catálogo en un diccionario ---- ")
    lineas = archivo.readlines()
    for linea in lineas[1:]:
        datos_producto = linea.strip().split(",")
        nombre = datos_producto[0]
        precio = datos_producto[1]
        cantidad = datos_producto[2]
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)
print("Catálogo cargado en diccionario exitosamente: ")
print(productos)

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

print("---- 5. Buscar un producto en la lista de productos ---- ")
nombre_producto_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_producto_buscado.lower():
        print("--- Producto Encontrado ---")
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"No se encontró el producto '{nombre_producto_buscado}'")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.
