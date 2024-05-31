libros = 10.99
frutas = 4.99
consolas = 199.99

descuento_usuario = int(input("Ingrese el descuento que desea aplicar en numero: "))
def descuento_productos(descuento):
    print(f"El precio original de los productos era:\nLibros: {libros}\nFrutas: {frutas}\nConsolas: {consolas}")
    print(f"El precio con el descuento del {descuento}% es:\nLibros: {round(libros - libros * descuento / 100, 2)}\nFrutas: {round(frutas - frutas * descuento / 100, 2)}\nConsolas: {round(consolas - consolas * descuento / 100, 2)}")
descuento_productos(descuento_usuario)