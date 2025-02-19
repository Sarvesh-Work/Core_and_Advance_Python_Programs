# Function to calculate factorial using while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    fact = 1
    while n > 0:
        fact *= n  # Multiply current number
        n -= 1  # Decrement number

    return fact

# Input from user
num = int(input("Enter a number: "))

# Call the function and print result
print(f"Factorial of {num} is: {factorial(num)}")
