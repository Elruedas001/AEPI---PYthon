def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]