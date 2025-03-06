def get_integer():
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid integer.")

# Call the function
try:
    get_integer()
except ValueError as e:
    print(e)



# Enter an integer: 10
# You entered: 10
