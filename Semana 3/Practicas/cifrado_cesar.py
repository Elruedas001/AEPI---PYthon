class CifradoCesar:
    def __init__(self, desplazamiento: int):
        self.desplazamiento = desplazamiento

    def cifrar(self, texto_claro: str) -> str:
        texto_cifrado = ""
        for char in texto_claro:
            if char.isalpha():
                desplazamiento_base = 65 if char.isupper() else 97
                texto_cifrado += chr((ord(char) - desplazamiento_base + self.desplazamiento) % 26 + desplazamiento_base)
            else:
                texto_cifrado += char
        return texto_cifrado

    def descifrar(self, texto_cifrado: str) -> str:
        texto_descifrado = ""
        for char in texto_cifrado:
            if char.isalpha():
                desplazamiento_base = 65 if char.isupper() else 97
                texto_descifrado += chr((ord(char) - desplazamiento_base - self.desplazamiento) % 26 + desplazamiento_base)
            else:
                texto_descifrado += char
        return texto_descifrado

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Cifrado César ---")
            print("1. Cifrar texto")
            print("2. Descifrar texto")
            print("3. Salir")
            eleccion = input("Selecciona una opción (1/2/3): ")

            if eleccion == "1":
                texto_claro = input("Introduce el texto claro: ")
                texto_cifrado = self.cifrar(texto_claro)
                print(f"Texto cifrado: {texto_cifrado}")
            elif eleccion == "2":
                texto_cifrado = input("Introduce el texto cifrado: ")
                texto_descifrado = self.descifrar(texto_cifrado)
                print(f"Texto descifrado: {texto_descifrado}")
            elif eleccion == "3":
                print("¡Gracias por usar el programa!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

# Ejemplo de uso
desplazamiento = 3  # Número de posiciones de desplazamiento para el cifrado César
cifrado_cesar = CifradoCesar(desplazamiento)
cifrado_cesar.mostrar_menu()
