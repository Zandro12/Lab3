
estudiantes = []

def agregar_usuario(carnet,nombre, edad,calificaciones):
    estudiante = {
        "carnet":carnet,
        "nombre": nombre,
        "edad": edad,
        "calificaciones":calificaciones

    }
    estudiantes.append(estudiante)

def buscar_usuario(carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet:
            return estudiante
    return None

def modificar_usuario(carnet, nuevo_nombre, nueva_edad):
    estudiante = buscar_usuario(carnet)
    if estudiante:
        estudiante["nombre"] = nuevo_nombre
        estudiante["edad"] = nueva_edad
        return True
    return False

def eliminar_usuario(carnet):
    estudiante = buscar_usuario(carnet)
    if estudiante:
        estudiantes.remove(estudiante)
        return True
    return False
