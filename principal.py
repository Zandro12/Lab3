

import gestor_estudiantes as gu

def mostrar_menu():
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar estudiante")
    print("4. Eliminar estudiante")
    print("5. Agregar calificaciones")
    print("6. Mostrar promedio de calificaciones")
    print("7. Mostrar lista de aprobados y reprobados")
    print("8. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            carnet = input("Carnet: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            calificaciones = input("Calificaciones: ")
            gu.agregar_estudiante(carnet, nombre, edad, calificaciones)

        elif opcion == "2":
            carnet = input("Carnet: ")
            estudiante = gu.buscar_estudiante(carnet)
            if estudiante:
                print(estudiante)
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            carnet = input("Carnet: ")
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            calificaciones = input("Calificaciones: ")
            if gu.modificar_estudiante(carnet, nombre, edad, calificaciones):
                print("Estudiante modificado.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            carnet = input("Carnet: ")
            if gu.eliminar_estudiante(carnet):
                print("Estudiante eliminado.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            carnet = input("Carnet: ")
            calificaciones = []
            while True:
                materia = input("Materia (o 'fin' para terminar): ")
                if materia.lower() == 'fin':
                    break
                nota = float(input("Nota: "))
                calificaciones.append((materia, nota))
            if gu.calificar_estudiante(carnet, calificaciones):
                print("Notas agregadas.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "6":
            carnet = input("Carnet: ")
            promedio = gu.promedio_calificaciones(carnet)
            print(f"Promedio de calificaciones: {promedio}")

        elif opcion == "7":
            aprobados, reprobados = gu.lista_aprobados_reprobados()
            print("Aprobados:")
            for estudiante in aprobados:
                print(estudiante)
            print("Reprobados:")
            for estudiante in reprobados:
                print(estudiante)

        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

