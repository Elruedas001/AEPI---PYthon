class Calculadora():
    def __init__(self):
        print("Las opciones que tienes para elegir son:\n0 --> Salir\n1 --> Sumar\n2 --> Restar\n3 --> Multiplicar\n4 --> Dividir")
        self.comprobar_opcion()
    def sumar(self):
        num1 = int(input("Elige el primer nr: "))
        num2 = int(input("Elige el segundo nr: "))
        resultado = num1+num2
        print(f"El resultado de sumar {num1} + {num2} es = {resultado}")
        return resultado
    def restar(self):
        num1 = int(input("Elige el primer nr: "))
        num2 = int(input("Elige el segundo nr: "))
        resultado = num1-num2
        print(f"El resultado de restar {num1} - {num2} es = {resultado}")
        return resultado
    def multiplicar(self):
        num1 = int(input("Elige el primer nr: "))
        num2 = int(input("Elige el segundo nr: "))
        resultado = num1*num2
        print(f"El resultado de multiplicar {num1} * {num2} es = {resultado}")
        return resultado
    def dividir(self):
        num1 = int(input("Elige el primer nr: "))
        num2 = int(input("Elige el segundo nr: "))
        resultado = num1/num2
        print(f"El resultado de dividir {num1} / {num2} es = {resultado}")
        return resultado
    def comprobar_opcion(self):
        while True:
            opcion = int(input("¿Que opcion quiere elegir? "))
            if opcion == 0:
                print("Gracias por su visita")
                break
            elif opcion == 1:
                self.sumar()
            elif opcion == 2:
                self.restar()
            elif opcion == 3:
                self.multiplicar()
            elif opcion == 4:
                self.dividir()
calculadora_01 = Calculadora()



