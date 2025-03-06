def read_file_line_by_line(filename="ABC.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")  # end="" avoids extra new lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_file_line_by_line()
