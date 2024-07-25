
estudiantes = []

def agregar_estudiante(carnet,nombre, edad,calificaciones):
    estudiante = {
        "carnet":carnet,
        "nombre": nombre,
        "edad": edad,
        "calificaciones":calificaciones

    }
    estudiantes.append(estudiante)

def buscar_estudiante(carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet:
            return estudiante
    return None

def modificar_estudiante(carnet, nombre, edad, calificaciones):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        estudiante["nombre"] = nombre
        estudiante["edad"] = edad
        estudiante["calificaciones"] = calificaciones
        return True
    return False

def eliminar_estudiante(carnet):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        estudiantes.remove(estudiante)
        return True
    return False
def calificar_estudiante(carnet, materia, nota):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        estudiante["calificaciones"].append({"materia": materia, "nota": nota})
        return True
    return False