def find_largest_and_smallest(lst):
 
    
    largest = smallest = lst[0]  # Initialize with first element

    for num in lst:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example list
numbers = [3, 7, 2, 8, 1, 9, 5]

# Calling the function
largest, smallest = find_largest_and_smallest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

# output: Largest number: 9
#         Smallest number: 1
