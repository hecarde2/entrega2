# Creamos la variable inventario que es igual a una lista vacia donde mas adelante se almacenaran datos 
inventario = []
#se crea la variable opcion que equivalente a 0 para que guarde la variable 
option = 0

#El while me permite crear un ciclo que se ejecuta si la variable opcion es diferente a 4 (salir)

while option != 4:

# Dentro del ciclo se muestra un menu a través de la funcion print 

    print("MENÚ DE INVENTARIO")
    print("1 AGREGAR PRODUCTO")
    print("2 MOSTRAR INVENTARIO")
    print("3 CALCULAR ESTADISTICAS")
    print("4 SALIR DEL SISTEMA")
# El usuario inserta la opcion que desee, para ello opcion es igual a numeros enteros el input que permite pedir el entero al usuario
    option = int(input("INGRESE UNA OPCIÓN: "))
# Si la opcion es igual a 1 se pide el nombre, precio y cantidad
    if option == 1:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
# se crea la varibale producto y en ella se almacena un diccionario donde guardaremos el nombre del producto, el precio y la cantidad
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
# Se agrega a lista ubicada en el principio en la variable inventario,  lo funcion que tiene es almacenar información del diccionario
# de la variable producto en la lista de la variable inventario y el print le muestra al usuario que esta fue añadida con exito. 
    
        inventario.append(producto)
        print("PRODUCTO AGREGADO CON EXITO.")
# Entonces si se selecciona la opcion 2, si se reccorre inventario y es 0 no hay productos
    # muestra si no hay productos
    elif option == 2:
        if len(inventario) == 0:
            print("NO HAY PRODUCTOS.")
# Pero si recorre inventario y si hay productos, le muestra al usuario los productos
        else:
            print("INVENTARIO")
            for producto in inventario:
                print(producto)
# se crea la option 3 con dos variables total de unidades y valor total donde a futuro serán usadas, son variables acomuladora donde se harán las operaciones
    # para ver el inventario
    elif option == 3:
        total_unidades = 0
        valor_total = 0

# Se recorre el diccionario dentro de la variable productos, que habia sido guardado en la lista de la variable inventario
# a la variable total_unidades sumale el valor que esta dentro del diccionario productos especificamente [cantidad]
# Lo que hara es sumar todas las cantidades ubicadas en el diccionario de producto y guardarlo en la variable total_unidades        
        for producto in inventario:
            total_unidades += producto["cantidad"]
# Lo que hara es sumar todas las cantidades ubicadas en el diccionario de producto en este caso producto ["precio"] y 
# mutiplicarlo por producto en este caso el valor["cantidad"]  y guardarlo en la variable valor_total
            valor_total += producto["precio"] * producto["cantidad"]
#posteriormente le muestra al cliente el total de unidades en general y el valor total del inventario 
        print("Total de unidades:", total_unidades)
        print("Valor total del inventario: $", valor_total)
# Si el usuario selecciona la opción 4,
# significa que desea finalizar la ejecución del programa
# Se muestra un mensaje de despedida.
# El ciclo while terminará automáticamente porque
# la condición del while es: while option != 4
# y ahora option vale 4, por lo tanto el ciclo se detiene.
    elif option == 4:
        print("HASTA PRONTO")
# se ejecuta cuando el usuario ingresa
# un número diferente a las opciones disponibles (1, 2, 3 o 4)
# Sirve como validación para evitar errores y
# obliga al usuario a intentar nuevamente.
# El programa NO se cierra y vuelve a mostrar el menú.

    else:
        print("VUELVE A INTENTAR")
