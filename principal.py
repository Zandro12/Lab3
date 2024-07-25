# principal.py

import gestor_estudiantes as gu


def mostrar_menu():
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            carnet=input("carnet:" )
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            calificaciones=input("Calificaciones:" )
            gu.agregar_usuario(carnet,nombre,edad,calificaciones)

        elif opcion == "2":
            carnet = input("Carnet: ")
            estudiante = gu.buscar_usuario(carnet)
            if estudiante:
                print(estudiante)
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            carnet = input("Carnet: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_edad = int(input("Nueva edad: "))
            if gu.modificar_usuario(carnet, nuevo_nombre, nueva_edad):
                print("Estudiante modificado.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            carnet = input("Carnet: ")
            if gu.eliminar_usuario(carnet):
                print("Estudiante eliminado.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
