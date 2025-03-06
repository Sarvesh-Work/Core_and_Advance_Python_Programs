def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))

divide_numbers(num1, num2)
