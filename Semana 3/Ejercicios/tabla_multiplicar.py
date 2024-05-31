def tabla_multiplicar(numero):
    resultado = ""
    for i in range(1, 11):
        resultado += f"{numero} * {i} = {numero * i}\n"
    return resultado

numero = int(input("Introduce un número del 1 al 10: "))
nombre_fichero = f"tabla-{numero}.txt"

with open(nombre_fichero, "w") as fichero:
    contenido = tabla_multiplicar(numero)
    fichero.write(contenido)

