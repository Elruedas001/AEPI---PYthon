class Triangulo:
    def __init__(self,lado_1,lado_2,lado_3):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
    def clasificar_triangulo(self):
        if self.lado_1 == self.lado_2 == self.lado_3:
            return "El triangulo es Equilatero"
        elif (self.lado_1 == self.lado_2) or (self.lado_2 == self.lado_3) or (self.lado_1 == self.lado_3):
            return "El triangulo es Isosceles"
        else:
            return "El triangulo es Escaleno"

triangulo_01 = Triangulo(11,15,12)
print(triangulo_01.clasificar_triangulo())