def son_anagramas(palabra_1, palabra_2):
    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()
    palabra_1_ordenada = sorted(palabra_1)
    palabra_2_ordenada = sorted(palabra_2)
    return palabra_1_ordenada == palabra_2_ordenada

palabra_1 = input("Escribe la primera palabra: ")
palabra_2 = input("Escribe la segunda palabra: ")

if son_anagramas(palabra_1, palabra_2) is True:
    print(f"Las palabras {palabra_1} y {palabra_2} son anagramas")
else:
    print(f"Las palabras {palabra_1} y {palabra_2} no son anagramas")