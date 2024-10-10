from decimal import Decimal
from decimal import InvalidOperation  
from calculator import Calculator
from calculator.commands import Command 



class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise InvalidOperation("Cannot divide by zero")
        result = Calculator.divide(self.a, self.b)
        return result
