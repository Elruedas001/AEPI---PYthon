class IntegerToRoman:
    def __init__(self):
        self.int_to_roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num: int) -> str:
        roman = ""
        for value, symbol in self.int_to_roman_map:
            while num >= value:
                roman += symbol
                num -= value
        return roman

converter = IntegerToRoman()
integer_number = 1994
roman_number = converter.convert(integer_number)
print(f"El número entero {integer_number} es igual a {roman_number} en números romanos.")
