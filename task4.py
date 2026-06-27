def calculator():
    print("--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter an operator (+, -, *, /, %): ").strip()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        elif operator == '%':
            if num2 == 0:
                return "Error: Modulo by zero is not allowed."
            result = num1 % num2
        else:
            return "Invalid operator selected."

        print(f"Result: {num1} {operator} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the program
calculator()