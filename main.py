import re
from decimal import Decimal, InvalidOperation
from calculator.commands import CommandHandler
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.menu import MenuCommand
from multiprocessing import Process, Queue

def worker(command_name, args, queue):
    """Worker function to execute commands in a separate process."""
    try:
        result = command_handler.execute_command(command_name, *args)
        queue.put(result)  # Put the result in the queue for retrieval
    except Exception as e:
        queue.put(f"An error occurred: {e}")

def main():
    global command_handler
    command_handler = CommandHandler()

    command_classes = {
        "add": AddCommand,
        "subtract": SubtractCommand,
        "multiply": MultiplyCommand,
        "divide": DivideCommand,
        "menu": MenuCommand,
    }

    for command_name, command_class in command_classes.items():
        command_handler.register_command(command_name, command_class)

    print("Welcome to the Calculator REPL!")
    print("Type commands like: add(1, 2), subtract(3, 1), etc.")
    print("Type 'menu' to list available commands.")
    print("Type 'exit' to exit.")

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break

        match = re.match(r"(\w+)(?:\(([^)]*)\))?", user_input)

        if match:
            command_name = match.group(1)
            args = match.group(2).split(",") if match.group(2) else []

            # Convert arguments to Decimal if present
            try:
                decimal_args = list(map(Decimal, args))
                queue = Queue()  # Create a queue to get results from the process
                process = Process(target=worker, args=(command_name, decimal_args, queue))
                process.start()  # Start the process
                process.join()  # Wait for the process to finish
                result = queue.get()  # Get the result from the queue

                # Print the result only if it is not a list (commands)
                if isinstance(result, list):  # Check if the result is a list (like menu)
                    print("Available commands:", ', '.join(result))
                else:
                    print(f"Result: {result}")

            except InvalidOperation:
                print("Invalid input. Please enter valid numbers.")
            except KeyError:
                print(f"No such command: {command_name}. Type 'menu' for available commands.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid command format")

if __name__ == '__main__':
    main()
