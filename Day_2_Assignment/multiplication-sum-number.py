def calculate_operations(a, b):
    multiplication = a * b
    summation = a + b
    return multiplication, summation

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate
product, total = calculate_operations(num1, num2)

# Output results
print(f"Multiplication: {product}")
print(f"Sum: {total}")
