import random
print("Este script se encarga de generar un password aleatorio")

longitud = int(input("¿De cuantos caracteres quieres que sea la contraseña?: "))
solo_letras = input("¿Quieres que solo tenga letras? (s/n): ")

if solo_letras == "s":
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = "".join(random.sample(letras, longitud))
    print(f"La contraseña generada es: {password}")
elif solo_letras == "n":
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.sample(letras, longitud))
    print(f"La contraseña generada es: {password}")
else:
    print("Opción no válida")
    exit()
