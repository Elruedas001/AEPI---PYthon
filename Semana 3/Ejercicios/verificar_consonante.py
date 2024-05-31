vocales = ["a","e","i","o","u"]
letra = input("Introduce una letra: ").lower()
def es_consonante(letra):
    if letra.isalpha() and len(letra) == 1:
        if letra in vocales:
            print(f"La letra {letra} no es consonante")
        else:
            print(f"La letra {letra} es consonante")
    else:
        print("Debes introducir un solo caracter y que sea una letra")

es_consonante(letra)
