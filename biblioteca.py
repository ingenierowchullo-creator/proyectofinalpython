# ==========================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA
# biblioteca.py
# ==========================================

import os

ARCHIVO = "biblioteca.txt"

libros = []


# ==========================================
# CARGAR DATOS
# ==========================================

def cargar_datos():
    global libros
    libros.clear()

    if not os.path.exists(ARCHIVO):
        return

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 7:

                libro = {
                    "codigo": datos[0],
                    "titulo": datos[1],
                    "autor": datos[2],
                    "categoria": datos[3],
                    "anio": int(datos[4]),
                    "cantidad": int(datos[5]),
                    "prestados": int(datos[6])
                }

                libros.append(libro)


# ==========================================
# GUARDAR DATOS
# ==========================================

def guardar_datos():

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:

        for libro in libros:

            archivo.write(
                f"{libro['codigo']};"
                f"{libro['titulo']};"
                f"{libro['autor']};"
                f"{libro['categoria']};"
                f"{libro['anio']};"
                f"{libro['cantidad']};"
                f"{libro['prestados']}\n"
            )


# ==========================================
# REGISTRAR LIBRO
# ==========================================

def registrar_libro():

    print("\n========== REGISTRAR LIBRO ==========\n")

    codigo = input("Código: ")

    for libro in libros:
        if libro["codigo"] == codigo:
            print("\nEl código ya existe.\n")
            return

    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")

    anio = int(input("Año: "))
    cantidad = int(input("Cantidad: "))

    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "anio": anio,
        "cantidad": cantidad,
        "prestados": 0
    }

    libros.append(libro)

    guardar_datos()

    print("\nLibro registrado correctamente.\n")


# ==========================================
# MOSTRAR LIBROS
# ==========================================

def mostrar_libros():

    print("\n============= LIBROS =============\n")

    if len(libros) == 0:
        print("No existen libros registrados.\n")
        return

    print("{:<8}{:<25}{:<18}{:<12}{:<12}".format(
        "Código",
        "Título",
        "Autor",
        "Disponibles",
        "Prestados"
    ))

    print("-" * 80)

    for libro in libros:

        disponibles = libro["cantidad"] - libro["prestados"]

        print("{:<8}{:<25}{:<18}{:<12}{:<12}".format(
            libro["codigo"],
            libro["titulo"],
            libro["autor"],
            disponibles,
            libro["prestados"]
        ))


# ==========================================
# BUSCAR LIBRO
# ==========================================

def buscar_libro():

    print("\n========== BUSCAR ==========\n")

    buscar = input("Ingrese código o título: ").lower()

    encontrado = False

    for libro in libros:

        if (buscar == libro["codigo"].lower() or
                buscar in libro["titulo"].lower()):

            disponibles = libro["cantidad"] - libro["prestados"]

            print("\nLibro encontrado")

            print("----------------------------")
            print("Código      :", libro["codigo"])
            print("Título      :", libro["titulo"])
            print("Autor       :", libro["autor"])
            print("Categoría   :", libro["categoria"])
            print("Año         :", libro["anio"])
            print("Cantidad    :", libro["cantidad"])
            print("Prestados   :", libro["prestados"])
            print("Disponibles :", disponibles)

            encontrado = True

    if not encontrado:
        print("\nLibro no encontrado.\n")


# ==========================================
# MODIFICAR LIBRO
# ==========================================

def modificar_libro():

    codigo = input("\nCódigo del libro: ")

    for libro in libros:

        if libro["codigo"] == codigo:

            print("\nIngrese los nuevos datos\n")

            libro["titulo"] = input("Título: ")
            libro["autor"] = input("Autor: ")
            libro["categoria"] = input("Categoría: ")
            libro["anio"] = int(input("Año: "))
            libro["cantidad"] = int(input("Cantidad: "))

            guardar_datos()

            print("\nLibro actualizado.\n")

            return

    print("\nNo existe el libro.\n")


# ==========================================
# ELIMINAR LIBRO
# ==========================================

def eliminar_libro():

    codigo = input("\nCódigo: ")

    for libro in libros:

        if libro["codigo"] == codigo:

            respuesta = input(
                "¿Desea eliminar el libro? (S/N): "
            ).upper()

            if respuesta == "S":

                libros.remove(libro)

                guardar_datos()

                print("\nLibro eliminado.\n")

            return

    print("\nLibro no encontrado.\n")

# ==========================================
# PRESTAR LIBRO
# ==========================================

def prestar_libro():

    print("\n========== PRÉSTAMO DE LIBRO ==========\n")

    codigo = input("Ingrese el código del libro: ")

    for libro in libros:

        if libro["codigo"] == codigo:

            disponibles = libro["cantidad"] - libro["prestados"]

            if disponibles > 0:

                libro["prestados"] += 1

                guardar_datos()

                print("\nPréstamo registrado correctamente.\n")

            else:

                print("\nNo existen ejemplares disponibles.\n")

            return

    print("\nLibro no encontrado.\n")


# ==========================================
# DEVOLVER LIBRO
# ==========================================

def devolver_libro():

    print("\n========== DEVOLUCIÓN ==========\n")

    codigo = input("Ingrese el código del libro: ")

    for libro in libros:

        if libro["codigo"] == codigo:

            if libro["prestados"] > 0:

                libro["prestados"] -= 1

                guardar_datos()

                print("\nDevolución registrada correctamente.\n")

            else:

                print("\nEse libro no tiene préstamos registrados.\n")

            return

    print("\nLibro no encontrado.\n")


# ==========================================
# ESTADÍSTICAS
# ==========================================

def estadisticas():

    print("\n========== ESTADÍSTICAS ==========\n")

    if len(libros) == 0:

        print("No existen libros registrados.\n")

        return

    total_libros = len(libros)

    total_ejemplares = 0

    total_prestados = 0

    libro_mayor = libros[0]

    libro_prestado = libros[0]

    for libro in libros:

        total_ejemplares += libro["cantidad"]

        total_prestados += libro["prestados"]

        if libro["cantidad"] > libro_mayor["cantidad"]:

            libro_mayor = libro

        if libro["prestados"] > libro_prestado["prestados"]:

            libro_prestado = libro

    disponibles = total_ejemplares - total_prestados

    print(f"Total de títulos registrados : {total_libros}")

    print(f"Total de ejemplares          : {total_ejemplares}")

    print(f"Total de préstamos           : {total_prestados}")

    print(f"Total disponibles            : {disponibles}")

    print()

    print("Libro con mayor cantidad")

    print("-------------------------")

    print(libro_mayor["titulo"])

    print(f"Ejemplares : {libro_mayor['cantidad']}")

    print()

    print("Libro más prestado")

    print("------------------")

    print(libro_prestado["titulo"])

    print(f"Préstamos : {libro_prestado['prestados']}")


# ==========================================
# PAUSA
# ==========================================

def pausar():

    input("\nPresione ENTER para continuar...")