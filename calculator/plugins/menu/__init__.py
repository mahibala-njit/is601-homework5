from calculator.commands import Command 

class MenuCommand(Command):
    def execute(self):
        return ["add", "subtract", "multiply", "divide", "menu", "exit"]  # Return list of commands
