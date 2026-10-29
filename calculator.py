class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

if __name__ == "__main__":
    calc = Calculator()
    print("Calculator initialized.")
    print("Example: 5 + 3 =", calc.add(5, 3))
    print("Example: 10 - 4 =", calc.subtract(10, 4))
    print("Example: 6 * 7 =", calc.multiply(6, 7))
    print("Example: 15 / 3 =", calc.divide(15, 3))
