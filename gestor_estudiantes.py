estudiantes=[]
def Agregar_estudiante(carnet,nombre,edad,grado,calificaciones=[]):
    estudiante={
        "carnet": carnet,
        "nombre": nombre,
        "edad": edad,
        "grado":grado,
    "calificaciones": calificaciones
    }
    estudiantes.append(estudiante)
def buscar_estudiante(carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet:
            return
def modificar_estudiante(carnet,nombre,edad,grado,calificaciones):
    estudiante = buscar_estudiante(carnet)
    if estudiante


