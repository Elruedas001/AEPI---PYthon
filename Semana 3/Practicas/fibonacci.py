class FibonacciSequence:
    def __init__(self, n: int):
        self.n = n

    def calculate(self) -> list:
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [0]
        elif self.n == 2:
            return [0, 1]

        sequence = [0, 1]
        for i in range(2, self.n):
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

n = 10
fibonacci = FibonacciSequence(n)
sequence = fibonacci.calculate()
print(f"Secuencia de Fibonacci de {n} términos: {sequence}")
    