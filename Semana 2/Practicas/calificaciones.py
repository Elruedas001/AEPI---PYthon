mensaje_inicio = print("Este script se encarga de pedir las notas y calcular su media")
asignaturas = []
notas = []
cantidad_asignaturas = int(input("¿Cuantas asignaturas tienes? "))
def solicitar_asignaturas(cantidad):
    for c in range(cantidad):
        asignatura = input("Introduce el nombre de la asignatura: ")
        asignaturas.append(asignatura)
def asignar_notas(asignaturas):
    for asignatura in asignaturas:
        nota = float(input(f"Introduce la nota de {asignatura}: "))
        notas.append(nota)
def calcular_media(notas):
    media = (sum(notas)) / len(notas)
    return round(media,2)
def aptitud(media):
    if media <5:
        return "Estas suspendido"
    elif media == 5:
        return "Tienes un suficiente"
    elif media == 6:
        return "Tienes un bien"
    elif media > 6 and media  <9:
        return "Tienes un notable"
    else:
        return print("Tienes un sobresaliente")

solicitar_asignaturas(cantidad_asignaturas)
asignar_notas(asignaturas)
print(f"Tu nota final es un {calcular_media(notas)}. {aptitud(calcular_media(notas))}")
    

