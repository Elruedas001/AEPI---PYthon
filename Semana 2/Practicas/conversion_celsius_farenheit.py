mensaje_inicio = print("Este programa permite la conversion de Celsius a Farenheit y viceversa")

def mostrar_menu():
    print("Elija una opcion:\n0 --> Salir\n1 --> Convertir de C a F\n2 --> Convertir de F a C\n3 --> Mostrar menu")

def celsius_fahrengeit(numero):
    farengeit = numero * (9/5) + 32
    return farengeit

def fahrengeit_celsius(numero):
    celsius = (numero - 32) * (5/9)
    return celsius
mostrar_menu()

while True:
    opcion_elegida = int(input("¿Que accion quieres realizar?: "))
    if opcion_elegida == 0:
        print("Gracias por su visita")
        break
    elif opcion_elegida == 1:
        numero = float(input("Introduce un numero: "))
        print(f"El resultado de pasar {numero} Celsius a Farengeit es: {round(celsius_fahrengeit(numero))} Grados")
    elif opcion_elegida == 2:
        numero = float(input("Introduce un numero: "))
        print(f"El resultado de pasar {numero} Farenheit a Celsius es: {round(fahrengeit_celsius(numero))} Grados")
    elif opcion_elegida == 3:
        mostrar_menu()
    else:
        print("Debes elegir una opcion valida")