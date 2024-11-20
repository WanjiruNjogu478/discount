class Calculator:
    def __init__(self, num1=22, num2=10):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


import math

print(math.pi)
print(math.sqrt(64))