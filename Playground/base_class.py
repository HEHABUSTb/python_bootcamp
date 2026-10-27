class BasicCalculator:
    def __init__(self, first_number: int, second_number: int):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number

calc = BasicCalculator(10, 5)

print(f"Addition: {calc.first_number} + {calc.second_number} = {calc.addition()}")
print(f"Subtraction: {calc.first_number} - {calc.second_number} = {calc.subtraction()}")
print(f"Multiplication: {calc.first_number} * {calc.second_number} = {calc.multiplication()}")
print(f"Division: {calc.first_number} / {calc.second_number} = {calc.division()}")
