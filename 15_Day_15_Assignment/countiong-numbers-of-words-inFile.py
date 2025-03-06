def count_words_in_file(filename="ABC.txt"):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()  # Splitting the text into words
            word_count = len(words)
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
count_words_in_file()
