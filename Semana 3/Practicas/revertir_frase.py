class ReversePhrase:
    def __init__(self, frase: str):
        self.frase = frase

    def reverse(self) -> str:
        words = self.frase.split()
        if len(words) != 2:
            raise ValueError("La frase debe contener exactamente dos palabras.")
        reversed_phrase = ' '.join(reversed(words))
        return reversed_phrase

frase = "Hola Chamo"
reverser = ReversePhrase(frase)
reversed_phrase = reverser.reverse()
print(f"Frase original: '{frase}'")
print(f"Frase invertida: '{reversed_phrase}'")
