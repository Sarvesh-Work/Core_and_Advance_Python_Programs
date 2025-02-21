def find_duplicates(lst):
    duplicates = []  # List to store duplicates
    for num in lst:
        if lst.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

# Hardcoded unordered list
numbers = [5, 9, 2, 5, 1, 8, 9, 6, 2, 7, 10, 3, 8, 2, 7]

# Print the duplicates
print("Duplicate values:", find_duplicates(numbers))

# output:Duplicate values: [5, 9, 2, 8, 7]