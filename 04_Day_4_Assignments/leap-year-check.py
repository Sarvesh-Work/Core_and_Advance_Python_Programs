def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Input from user
year = int(input("Enter a year: "))

# Check and print result
print(f"{year} is a leap year" if is_leap_year(year) else f"{year} is not a leap year")
