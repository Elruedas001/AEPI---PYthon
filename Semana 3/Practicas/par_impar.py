class VerificadorParidad:
    def __init__(self, numero: int):
        self.numero = numero

    def es_par(self) -> bool:
        return self.numero % 2 == 0

    def es_impar(self) -> bool:
        return self.numero % 2 != 0

    def verificar_paridad(self) -> str:
        if self.es_par():
            return f"El número {self.numero} es par."
        else:
            return f"El número {self.numero} es impar."

numero = 7
verificador = VerificadorParidad(numero)
resultado = verificador.verificar_paridad()
print(resultado)
