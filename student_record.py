# Student Management System

# List to store student information
students = []

# Function to add a student
def add_student():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    school = input("Enter the student's school: ")
    student = {
        'name': name,
        'age': age,
        'school': school
    }
    students.append(student)
    print(f"\n{name} has been added successfully!\n")

# Function to view all students
def view_students():
    if len(students) == 0:
        print("No students to display!\n")
        return
    
    print("\nList of Students:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} - Age: {student['age']}, School: {student['school']}")
    print("\n")

# Function to search for a student by name
def search_student():
    search_name = input("\nEnter the name of the student to search for: ")
    found = False
    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"\nStudent Found: {student['name']} - Age: {student['age']}, School: {student['school']}\n")
            found = True
            break
    if not found:
        print(f"\nNo student found with the name '{search_name}'\n")

# Function to display the menu
def display_menu():
    print("\nStudent Management System")
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice, please try again!\n")
