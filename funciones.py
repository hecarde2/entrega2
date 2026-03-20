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