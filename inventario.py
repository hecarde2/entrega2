# importar las funciones desde archivo funciones.py
from funciones import *
# Creamos la variable inventario que es igual a una lista vacia donde mas adelante se almacenaran datos 
inventario = []
#se crea la variable opcion que equivalente a 0 que se usara mas adelante
option = 0

#El while me permite crear un ciclo que se ejecuta si la variable opcion es diferente a 4 (salir)

while option != 4:
# Imprimir en la pantalla del usuario el menú, el menú ya esta en funciones 
    mostrar_menu()

# El usuario inserta la opcion que desee, para ello opcion es igual a numeros enteros el input que permite pedir el entero al usuario
    option = int(input("INGRESE UNA OPCIÓN: "))
# Si la opcion es igual a 1 se pide el nombre, precio y cantidad
# se crea la varibale producto que esta en documento de funciones y en ella se almacena un diccionario donde guardaremos el nombre del producto, el precio y la cantidad
# se crea la varibale producto y en ella se almacena un diccionario donde guardaremos el nombre del producto, el precio y la cantidad
# Se agrega a lista ubicada en el principio en la variable inventario,  lo funcion que tiene es almacenar información del diccionario
# de la variable producto en la lista de la variable inventario y el print le muestra al usuario que esta fue añadida con exito. 
    
    if option == 1:
       agregar_producto(inventario)

# Entonces si se selecciona la opcion 2, si se reccorre inventario y es 0 no hay productos
    # muestra si no hay productos
    # Pero si recorre inventario y si hay productos, le muestra al usuario los productos
    elif option == 2:
        mostrar_inventario(inventario)
# se crea la option 3 con dos variables total de unidades y valor total donde a futuro serán usadas, son variables acomuladora donde se harán las operaciones
    # para ver el inventario
    elif option == 3:
        calcular_estadisticas(inventario)
       
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

# El objetivo de la semana: Importar desde otro archivo PY funciones para un codigo limpio, presentar un menú al usuario.
# A nivel de desarrollador el llamar variables en funciones.