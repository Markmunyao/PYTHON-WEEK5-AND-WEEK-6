# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("12345\n")
    file.write("This is line 3 with some numbers: 42, 7, and 9.\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    print("Contents of my_file.txt:")
    for line in file:
        print(line.strip())

# File Appending
with open("my_file.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("Appending some numbers: 10, 20, and 30.\n")
    file.write("This is the last line appended.\n")

# Error Handling
try:
    with open("non_existing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Finished handling errors.")
