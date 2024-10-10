from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command  

class SubtractCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self):
        result = Calculator.subtract(self.a, self.b)
        return result

