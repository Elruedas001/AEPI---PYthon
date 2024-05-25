print("Este programa se encarga de calcular el IMC (Indice de Masa Corporal)")

def solicitar_datos():
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))
    return peso, altura

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"tu indice de masa corporal es: {round(imc, 2)}")
    return imc

def diagnosticar(imc):
    if imc < 18.5:
        print("Tienes bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Tu peso es normal")
    elif imc >= 25 and imc <= 29.9:
        print("Tienes sobrepeso")
    else:
        print("Tienes obesidad")

peso, altura = solicitar_datos()
imc = calcular_imc(peso, altura)
diagnosticar(imc)
