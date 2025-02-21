# question === 
# 1. Write a Python program to Count all letters, digits, and special symbols from the given 

# string Input = “P@#yn26at^&i5ve”

#  Output: Chars = 8 Digits = 2 Symbol = 3 


# code--->

# Define the input string
input_str = "P@#yn26at^&i5ve"

# Initialize counters for characters, digits, and special symbols
char_count = 0
digit_count = 0
symbol_count = 0

# Loop through each character in the string
for char in input_str:
    # Check if the character is a letter
    if char.isalpha():
        char_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit_count += 1
    # Otherwise, it's a special symbol
    else:
        symbol_count += 1

# Print the results
print("Chars =", char_count)
print("Digits =", digit_count)
print("Symbols =", symbol_count)

# Output: Chars = 8 Digits = 2 Symbols = 3