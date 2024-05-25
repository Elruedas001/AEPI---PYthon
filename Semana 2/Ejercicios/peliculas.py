print("Las opciones que tiene son las siguientes:\n0 --> Salir\n1 --> Consultar pelicula\n2 --> Consultar sala")
print("Las peliculas que hay son las siguientes:\nAvengers\nStars Wars\nMatrix")
print("Las salas que hay son las siguientes:\nSala 1\nSala 2\nSala 3")

datos = {1:"Avengers",2:"Star Wars",3:"Matrix"}

def mostrar_pelicula(sala):
    for s in datos.keys():
        if s == sala:
            return datos[s]
    return "Sala no encontrada"

def mostrar_sala(pelicula):
    for s,p in datos.items():
        if p == pelicula:
            return s
    return "Pelicula no encontrada"

while True:
    print("Recuerde que las opciones que tiene son:\n0 --> Salir\n1 --> Consultar pelicula\n2 --> Consultar sala")
    opcion_usuario = int(input("¿Qué opción desea elegir?: "))

    if opcion_usuario == 0:
        print("Ha sido un placer majo")
        break
    elif opcion_usuario == 1:
        pelicula_consultada = input("¿Qué película quiere consultar: ")
        print(f"La pelicula {pelicula_consultada} se emite en la sala {mostrar_sala(pelicula_consultada)}")
    elif opcion_usuario == 2:
        sala_consultada = int(input("¿Qué sala quiere consultar?: "))
        print(f"En la sala {sala_consultada} se emite la palicula {mostrar_pelicula(sala_consultada)}")
    else:
        print("Debe elegir una opcion valida")


