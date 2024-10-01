# Get user input for a number
number = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Use a for loop to print numbers from 1 to the entered number
print("Here are the numbers from 1 to", number)
for i in range(1, number + 1):
    print(i)

# Use a while loop to print the same numbers in reverse
print("Here are the numbers from", number, "to 1 in reverse")
while number > 0:
    print(number)
    number -= 1  # Decrement the number by 1
