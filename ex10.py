# File Handling Tutorial in Python
# This file covers reading, writing, appending, exception handling, and context managers

# Writing to a file
# 'w' mode is used for writing. If the file does not exist, it will be created.
# If the file exists, its content will be overwritten.
def write_to_file():
    with open("example1.txt", "w") as file:
        file.write("Hello, boss!\n")
        file.write("This is a file handling tutorial in Python.\n")
        file.write("We are learning how to write, read, and handle errors gracefully.")
    print("Data written to file successfully.")

# Reading from a file
# 'r' mode is used for reading. It reads the content of the file.
# If the file does not exist, a FileNotFoundError will be raised.
def read_from_file():
    try:
        with open("example1.txt", "r") as file:
            contents = file.read()
        print("File content:")
        print(contents)
    except FileNotFoundError:
        print("The file 'example.txt' does not exist!")

# Appending to a file
# 'a' mode is used for appending. It adds content to the file without overwriting it.
def append_to_file():
    with open("example1.txt", "a") as file:
        file.write("\nWe are appending this line to the file.")
    print("Data appended to file successfully.")

# Reading file line by line
# You can also read a file line by line using a loop.
def read_file_line_by_line():
    try:
        with open("example1.txt", "r") as file:
            print("Reading file line by line:")
            for line in file:
                print(line.strip())  # .strip() removes extra newlines
    except FileNotFoundError:
        print("The file 'example.txt' does not exist!")

# Handling exceptions
# Demonstrating how to handle errors gracefully with try-except.
def exception_handling_demo():
    try:
        with open("non_existent_file.txt", "r") as file:
            contents = file.read()
        print(contents)
    except FileNotFoundError:
        print("The file you are trying to open does not exist!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Word Frequency Program
# This program reads a text file and counts the frequency of each word in the file.
from collections import Counter

def word_frequency_counter(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        # Remove punctuation and convert to lowercase
        words = content.lower().split()

        # Count the frequency of each word
        word_count = Counter(words)

        # Print the word frequencies
        print("Word frequency count:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to demonstrate all file handling operations
def main():
    print("\n--- Writing to a File ---")
    write_to_file()

    print("\n--- Reading from a File ---")
    read_from_file()

    print("\n--- Appending to a File ---")
    append_to_file()

    print("\n--- Reading File Line by Line ---")
    read_file_line_by_line()

    print("\n--- Exception Handling Demo ---")
    exception_handling_demo()

    print("\n--- Word Frequency Counter ---")
    word_frequency_counter("example.txt")

# Run the main function to see everything in action
if __name__ == "__main__":
    main()
