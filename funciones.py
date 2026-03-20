def mostrar_menu():
    print("MENÚ DE INVENTARIO")
    print("1 AGREGAR PRODUCTO")
    print("2 MOSTRAR INVENTARIO")
    print("3 CALCULAR ESTADISTICAS")
    print("4 SALIR DEL SISTEMA")


def agregar_producto(inventario):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        if precio < 0:
              print("Numero invalido")
        if cantidad < 0:
              print("Numero invalido")

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

    
        inventario.append(producto)
        print("PRODUCTO AGREGADO CON EXITO.")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
            print("NO HAY PRODUCTOS.")

    else:
         print("INVENTARIO")
         for producto in inventario:
            print(producto)


def  calcular_estadisticas(inventario):
        total_productos_registrados = 0
        valor_total = 0        
        for producto in inventario:
            total_productos_registrados = len(inventario)

            valor_total += producto["precio"] * producto["cantidad"]

        print("Total de productor:", total_productos_registrados)
        print("Valor total del inventario: $", valor_total)