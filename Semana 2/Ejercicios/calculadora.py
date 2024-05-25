from mis_modulos.aritmetica import suma,resta,multiplicar,dividir,ingresar_numeros

print("""Elige una de las siguientes opciones:
0  --> Salir
1 --> Sumar 2 numeros
2 --> Restar 2 numeros
3 --> Multiplicar 2 numeros
4 --> Dividir 2 numeros""")

while True:
    print("Para mostrar el menu escribe 5")
    opcion = int(input("¿Que opciones eliges? "))
    if opcion == 0:
        print("Gracias por tu visita Chamo")
        break
    elif opcion == 1:
        a,b = ingresar_numeros()
        print(f"El resultado de sumar {a} + {b} es {suma(a,b)}")
    elif opcion == 2:
        a,b = ingresar_numeros()
        print(f"El resultado de restar {a} - {b} es {resta(a,b)}")
    elif opcion == 3:
        a,b = ingresar_numeros()
        print(f"El resultado de multiplicar {a} * {b} es {multiplicar(a,b)}")
    elif opcion == 4:
        a,b = ingresar_numeros()
        print(f"El resultado de dividir {a} / {b} es {dividir(a,b)}")
    elif opcion == 5:
        print("""
0  --> Salir
1 --> Sumar 2 numeros
2 --> Restar 2 numeros
3 --> Multiplicar 2 numeros
4 --> Dividir 2 numeros""")
    else:
        print("Debes elegir una opción válida")