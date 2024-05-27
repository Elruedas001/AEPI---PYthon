print("Este programa permite el registro y el manejo de contactos")
def mostrar_menu():
    print("Elija una opcion:\n0 --> Salir\n1 --> Agregar contacto\n2 --> Buscar contacto\n3 --> Mostrar contactos\n4 --> Eliminar contacto\n5 --> Mostrar menu")

def agregar_contacto(nombre, telefono, email, contactos):
    contacto = {"Nombre": nombre, "Telefono": telefono, "Email": email}
    contactos[nombre] = contacto
    mostrar_nombre = contacto["Nombre"]
    mostrar_telefono = contacto["Telefono"]
    mostrar_email = contacto["Email"]
    mensaje = print(f"Se ha agregado el contacto: {mostrar_nombre}, {mostrar_telefono}, {mostrar_email}")
    return mensaje

def buscar_contacto(nombre, contactos):
    if nombre in contactos:
        return contactos[nombre]
    mensaje = print(f"No se ha encontrado el contacto {nombre}")
    return mensaje

def eliminar_contacto(nombre, contactos):
    if nombre in contactos:
        contacto_eliminado = contactos.pop(nombre)
        mensaje = print(f"Se ha eliminado el contacto {contacto_eliminado}")
        return mensaje

def mostrar_contactos(diccionario):
    for contacto in diccionario.values():
        nombre = contacto["Nombre"]
        telefono = contacto["Telefono"]
        email = contacto["Email"]
        print(f"Nombre: {nombre}, Telefono: {telefono}, Email: {email}")


diccionario_contactos = {}
mostrar_menu()
while True:
    opcion_elegida = int(input("¿Qué desea hacer?: "))
    if opcion_elegida == 0:
        print("Gracias por su visita")
        break
    elif opcion_elegida == 1:
        nombre = input("Introduce el nombre del contacto: ")
        telefono = int(input("Introduce el telefono del contacto: "))
        email = input("Introduce el email del contacto: ")
        agregar_contacto(nombre, telefono, email, diccionario_contactos)
    elif opcion_elegida == 2:
        nombre = input("¿Cómo se llama a quien buscas?: ")
        print(buscar_contacto(nombre, diccionario_contactos))
    elif opcion_elegida == 3:
        mostrar_contactos(diccionario_contactos)
    elif opcion_elegida == 4:
        nombre_eliminado = input("¿Que nombre quieres eliminar? ")
        eliminar_contacto(nombre_eliminado,diccionario_contactos)
    elif opcion_elegida == 5:
        mostrar_menu()
    else:
        print("Debes escoger una opcion valida")

