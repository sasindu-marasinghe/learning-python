# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, boss!\n")
    file.write("Welcome to file handling in Python.")
file = open("example.txt","r")
print(file.read())
