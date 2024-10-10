# calculator/commands/add/__init__.py

from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command  

class AddCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self):
        result = Calculator.add(self.a, self.b)
        return result

