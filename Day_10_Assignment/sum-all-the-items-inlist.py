# Function to calculate the sum of all elements in a list
def sum_of_list(lst):
    total = 0  # Initialize sum variable to 0
    
    # Loop through each element in the list
    for num in lst:
        total += num  # Add each element to total
    
    return total  # Return the final sum

# Example list
numbers = [1, 2, 3, 4, 5]

# Calling the function and printing the result
result = sum_of_list(numbers)
print("Sum of all items in the list:", result)

# output :Sum of all items in the list: 15