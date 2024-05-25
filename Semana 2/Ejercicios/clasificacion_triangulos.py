print("Aqui vamos a calcular si un triangulo es equilatero, escaleno o isosceles. Para ello tienes que darme las longitudes de los lados")
while True:
    print("Si quieres salir marca 0, si quieres calcular los lados marca 1")
    opcion_elegida = int(input("¿Que opcion quieres marcar? "))
    if opcion_elegida == 0:
        print("Gracias por su visita)")
        break
    elif opcion_elegida == 1:
        long_lado_1 = int(input("Introduce la longitud del primer lado: "))
        long_lado_2 = int(input("Introduce la longitud del segundo lado: "))
        long_lado_3 = int(input("Introduce la longitud del tercer lado: "))
        if long_lado_1 == long_lado_2 == long_lado_3:
            resultado = "Equilatero"
            print(f"El triangulo es {resultado}")
        elif (long_lado_1 == long_lado_2) or (long_lado_2 == long_lado_3) or long_lado_1 == long_lado_3:
            resultado = "Isosceles"
            print(f"El triangulo es {resultado}")
        else:
            resultado = "Escaleno"
            print(f"El triangulo es {resultado}")
    else:
        print("Debes escoger una opcion valida")
