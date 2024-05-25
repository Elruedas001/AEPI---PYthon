class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 

    def mostrar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad,):
        super().__init__(nombre, apellido, edad)
        self.sueldo = int(input(f"Introduce tu sueldo {self.nombre} {self.apellido}: "))

    def mostrar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y mi sueldo es de {self.sueldo}€ anuales")
        

    def pagar_impuestos(self):
        if self.sueldo > 15000:
            print("Debes pagar impuestos")
        else:
            print("No debes pagar un '20%' en impuestos")


persona_01 = Persona("Denis","Florin",23)
persona_02 = Persona("Laura","Rojas",34)

persona_01.mostrar()
persona_02.mostrar()

empleado_01 = Trabajador("Luis","Perez",52)
empleado_01.mostrar()
empleado_01.pagar_impuestos()
