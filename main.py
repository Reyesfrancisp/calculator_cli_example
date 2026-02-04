import sys
from Calculator import add, subtract, multiply, divide

def calculate_and_print(a, b, operation_name, operation_func):
    try:
        result = operation_func(a, b)
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Welcome to the Interactive Calculator CLI!")
    print("Type 'exit' to quit.")
    
    while True:
        command = input("\nEnter command (add, subtract, multiply, divide): ").strip().lower()
        
        if command == 'exit':
            print("Goodbye!")
            sys.exit()
            
        if command not in ['add', 'subtract', 'multiply', 'divide']:
            print("Unknown command. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if command == 'add':
            calculate_and_print(num1, num2, "add", add)
        elif command == 'subtract':
            calculate_and_print(num1, num2, "subtract", subtract)
        elif command == 'multiply':
            calculate_and_print(num1, num2, "multiply", multiply)
        elif command == 'divide':
            calculate_and_print(num1, num2, "divide", divide)

if __name__ == '__main__':
    main()