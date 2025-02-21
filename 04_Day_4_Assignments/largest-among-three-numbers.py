# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Find the largest using ternary operator
largest = a if (a > b and a > c) else (b if b > c else c)

# Print the result
print(f"The largest number is: {largest}")
