import random

class JuegoPiedraPapelTijera:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera"]
        self.resultados = {
            ("piedra", "tijera"): "ganas",
            ("papel", "piedra"): "ganas",
            ("tijera", "papel"): "ganas",
            ("tijera", "piedra"): "pierdes",
            ("piedra", "papel"): "pierdes",
            ("papel", "tijera"): "pierdes",
        }

    def jugar(self):
        while True:
            print("\n--- Menú de Juego Piedra, Papel y Tijera ---")
            print("1. Jugar")
            print("2. Salir")
            eleccion = input("Selecciona una opción (1/2): ")

            if eleccion == "1":
                self.jugar_ronda()
            elif eleccion == "2":
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def jugar_ronda(self):
        jugador = input("Elige piedra, papel o tijera: ").lower()
        if jugador not in self.opciones:
            print("Opción no válida. Inténtalo de nuevo.")
            return

        computadora = random.choice(self.opciones)
        print(f"Computadora eligió: {computadora}")

        if jugador == computadora:
            resultado = "empate"
        else:
            resultado = self.resultados.get((jugador, computadora), "pierdes")

        if resultado == "empate":
            print("Es un empate.")
        elif resultado == "ganas":
            print("¡Tú ganas!")
        else:
            print("Tú pierdes.")

juego = JuegoPiedraPapelTijera()
juego.jugar()
