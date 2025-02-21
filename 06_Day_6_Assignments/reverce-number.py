# Function to reverse a number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = (reversed_num * 10) + digit  # Append digit to reversed number
        n //= 10  # Remove the last digit
    return reversed_num

# Input from user
num = int(input("Enter a number: "))

# Call the function and print result
reversed_result = reverse_number(num)
print(f"Reversed number: {reversed_result}")
