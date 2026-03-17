inventario = []
option = 0

while option != 4:

    print("MENÚ DE INVENTARIO")
    print("1 AGREGAR PRODUCTO")
    print("2 MOSTRAR INVENTARIO")
    print("3 CALCULAR ESTADISTICAS")
    print("4 SALIR DEL SISTEMA")

    option = int(input("INGRESE UNA OPCIÓN: "))

    if option == 1:
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

    elif option == 2:
        if len(inventario) == 0:
            print("NO HAY PRODUCTOS.")
        else:
            print("INVENTARIO")
            for producto in inventario:
                print(producto)

    elif option == 3:
        total_unidades = 0
        valor_total = 0

        for producto in inventario:
            total_unidades += producto["cantidad"]
            valor_total += producto["precio"] * producto["cantidad"]

        print("Total de unidades:", total_unidades)
        print("Valor total del inventario: $", valor_total)

    elif option == 4:
        print("HASTA PRONTO")

    else:
        print("VUELVE A INTENTAR")
