# Function to perform division
def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function and print result
result = div(num1, num2)
print(f"Division result: {result}")
