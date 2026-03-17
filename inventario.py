#Programa de inventario

#Empezamos dandole la bienvenida al usuario al programa 

print("bienvenido al sistema de inventario")

#Continuamos pidiendole los datos del producto al usuario(nombre del producto, precio y cantidad)


nombre=input("nombre del producto : ")


#Usamos el while true en esta posicion para que en caso de que el usuario ingrese un valor no valido para el precio o la cantidad,
#Se le pedira que ingrese un valor valido sin tener que volver a ingresar el nombre del producto.


while True:
    precio=float(input("Ingrese el precio del producto: $ "))
    cantidad=int(input("Ingrese la cantidad del producto:  "))

    #Colocamos condiciones que queremos que se cumplan, en este caso que el precio y la cantidad sean numeros positivos, 
    #Si no se cumplen se le dara un mensaje de error al usuario y se le pedira que ingrese un valor valido.

    if precio < 0:
        print("Error: El precio y la cantidad deben ser números positivos.ejemplo(1, 2, 3...)")
        print("Por favor, ingrese un precio válido.")
    elif cantidad < 0:
        print("Error: El precio y la cantidad deben ser números positivos.(ejemplo: 1, 2, 3...)")
        print("Por favor, ingrese una cantidad válida.")
        break

    #Si se cumplen las condiciones Y el numero ingrsado es positivo, se le mostrara el total del inventario y los datos del producto ingresados por el usuario.


    else:
        costo_total=precio*cantidad
        print("El total del inventario es: $", costo_total)
                

        print(f"nombre del producto: {nombre}")
        print(f"precio del producto: $ {precio}")
        print(f"cantidad del producto: {cantidad}")
        print(f"costo total: $ {costo_total}")
        break


#Este programa es un sistema de inventario simple que permite al usuario ingresar el nombre, precio 
#y cantidad de un producto, y luego calcula el costo total del inventario.
#El programa también incluye validaciones para asegurarse de que el precio y la cantidad sean números positivos.
