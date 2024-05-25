from mis_modulos.textos import es_palindromo

palabra = input("Introduce una palabra: ")

if es_palindromo(palabra) is True:
    print(f"La palabra {palabra} es palindroma")
else:
    print(f"La palabra {palabra} no es palíndroma")