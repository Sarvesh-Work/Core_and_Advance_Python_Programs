# Function to check if a number is palindrome
def is_palindrome(n):
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10  # Get last digit
        reversed_num = (reversed_num * 10) + digit  # Append digit to reversed number
        n //= 10  # Remove last digit

    return original == reversed_num  # Check if original and reversed numbers are the same

# Input from user
num = int(input("Enter a number: "))

# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
