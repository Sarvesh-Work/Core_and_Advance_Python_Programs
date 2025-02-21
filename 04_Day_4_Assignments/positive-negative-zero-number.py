# Input from user
num = float(input("Enter a number: "))

# Check and print result using ternary operator
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

print(f"The number is {result}.")
