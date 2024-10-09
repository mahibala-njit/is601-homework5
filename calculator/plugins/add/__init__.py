# calculator/commands/add/__init__.py

from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command  # Ensure this import path is correct

class AddCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self):
        result = Calculator.add(self.a, self.b)
        print(f"Result: {result}")
        return result
