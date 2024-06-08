class RomanAInteger:
    def __init__(self):
        self.roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convertidor(self, roman: str) -> int:
        total = 0
        prev_value = 0

        for char in reversed(roman):
            value = self.roman_to_int_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total

converter = RomanAInteger()
roman_number = "MCMXCIV"
integer_number = converter.convertidor(roman_number)
print(f"El número romano {roman_number} es igual a {integer_number} en números enteros.")
