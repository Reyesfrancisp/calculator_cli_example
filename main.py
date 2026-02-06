import sys
from calculator_cli import add, subtract, multiply, divide

def calculate_and_print(a, b, operation_name, operation_func):
    # Map command names to standard math symbols
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    
    # Get the symbol, or default to the name if something goes wrong
    symbol = symbols.get(operation_name, operation_name)
    
    try:
        result = operation_func(a, b)
        # Prints cleaner output: 10 + 5 = 15
        print(f"{a} {symbol} {b} = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Welcome to the Interactive Calculator CLI!")
    print("Type 'exit' to quit.")
    
    # Dictionary mapping strings to functions
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    while True:
        command = input("\nEnter command (add, subtract, multiply, divide): ").strip().lower()
        
        if command == 'exit':
            print("Goodbye!")
            sys.exit()
            
        if command not in operations:
            print("Unknown command. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        calculate_and_print(num1, num2, command, operations[command])

if __name__ == '__main__':
    main()
