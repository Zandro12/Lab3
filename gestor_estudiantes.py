estudiantes = []

def agregar_estudiante(carnet, nombre, edad, calificaciones):
    estudiante = {
        "carnet": carnet,
        "nombre": nombre,
        "edad": edad,
        "calificaciones": []
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

def calificar_estudiante(carnet, calificaciones):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        for calificacion in calificaciones:
            materia, nota = calificacion
            estudiante["calificaciones"].append({"materia": materia, "nota": nota})
        return True
    return False

def promedio_calificaciones(carnet):
    estudiante = buscar_estudiante(carnet)
    if estudiante and estudiante["calificaciones"]:
        total = sum(calificacion["nota"] for calificacion in estudiante["calificaciones"])
        return total / len(estudiante["calificaciones"])
    return 0

def lista_aprobados_reprobados():
    aprobados = []
    reprobados = []
    for estudiante in estudiantes:
        promedio = promedio_calificaciones(estudiante["carnet"])
        if promedio >= 7:
            aprobados.append(estudiante)
        else:
            reprobados.append(estudiante)
    return aprobados, reprobados


