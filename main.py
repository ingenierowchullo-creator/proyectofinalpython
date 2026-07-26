from biblioteca import *

cargar_datos()

while True:

    print("\n")
    print("=" * 45)
    print("     SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 45)
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Modificar libro")
    print("5. Eliminar libro")
    print("6. Prestar libro")
    print("7. Devolver libro")
    print("8. Estadísticas")
    print("9. Salir")
    print("=" * 45)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        registrar_libro()
        pausar()

    elif opcion == "2":

        mostrar_libros()
        pausar()

    elif opcion == "3":

        buscar_libro()
        pausar()

    elif opcion == "4":

        modificar_libro()
        pausar()

    elif opcion == "5":

        eliminar_libro()
        pausar()

    elif opcion == "6":

        prestar_libro()
        pausar()

    elif opcion == "7":

        devolver_libro()
        pausar()

    elif opcion == "8":

        estadisticas()
        pausar()

    elif opcion == "9":

        print("\nGracias por utilizar el sistema.")

        break

    else:

        print("\nOpción incorrecta.")