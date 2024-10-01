# Reading from a file
file = open("file.txt","r")
print(file.read())


file = open("file.txt","a")
file.write("\n Sasindu thamei game inne")
file.write("\n sasindu bothayek....")

file = open("file.txt","r")

print(file.read())
file.close()
