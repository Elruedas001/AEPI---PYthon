tareas = []

def mostrar_menu():
    print("\nMenú de opciones:")
    print("a) Agregar tarea")
    print("b) Marcar tarea como completada")
    print("c) Ver tareas pendientes")
    print("d) Salir")

def agregar_tarea():
    tarea = input("¿Que tarea quiere añadir?: ")
    tareas.append({'tarea': tarea, 'completada': False})
    print(f"Ha añadido la tarea: {tarea}")

def ver_tareas_pendientes():
    print("\nTareas pendientes:")
    for i, tarea in enumerate(tareas):
        if not tarea['completada']:
            print(f"{i}. {tarea['tarea']}")
    if not any(not tarea['completada'] for tarea in tareas):
        print("No hay tareas pendientes.")

def marcar_completada():
    ver_tareas_pendientes()
    if not tareas:
        print("No hay tareas pendientes.")
        return
    num_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
    if 0 <= num_tarea < len(tareas):
        tareas[num_tarea]['completada'] = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == 'a':
        agregar_tarea()
    elif opcion == 'b':
        marcar_completada()
    elif opcion == 'c':
        ver_tareas_pendientes()
    elif opcion == 'd':
        print("Saliendo del programa.")
        break
    else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

