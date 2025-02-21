# question=
# 2. Write a Python program to remove duplicate characters of a given string. 

# Input = “String and String Function” 

# Output: String and Function


# code--->

# Define the input string
input_str = "String and String Function"

# Initialize an empty string to store unique characters
result = ""

# Use a set to track seen characters
seen_chars = set()

# Loop through each character in the string
for char in input_str:
    # If character is not in seen set, add it to result and mark as seen
    if char not in seen_chars:
        result += char
        seen_chars.add(char)

# Print the result
print("Output:", result)

# Output: String and Function