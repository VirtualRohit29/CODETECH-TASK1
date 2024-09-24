# Initializing dictionary
student_grades = {}

# Add a new student
def add_student(name, grade):
    if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
        student_grades[name] = grade
        print(f"Added {name} with a grade {grade}")
        if grade == 'F':
            print(f"{name} has failed.")
        else:
            print(f"{name} has passed.")
    else:
        print("Invalid grade! Please enter a grade from A to F.")

# Update a student
def update_student(name, grade):
    if name in student_grades:
        if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            student_grades[name] = grade
            print(f"{name}'s marks have been updated to {grade}")
            if grade == 'F':
                print(f"{name} has failed.")
            else:
                print(f"{name} has passed.")
        else:
            print("Invalid grade! Please enter a grade from A to F.")
    else:
        print(f"{name} is not found!")

# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} is not found!")

# View all students
def display_all_students():
    if student_grades:
        print("\nAll students and their grades:")
        for name, grade in student_grades.items():
            status = "Passed" if grade != 'F' else "Failed"
            print(f"{name}: {grade} - {status}")
    else:
        print("No students found/added.")

# Main function
def main():
    while True:
        print('\nStudent Grades Management System')
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View all students")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = input("Enter student grade (A-F) = ").upper()
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name = ")
            grade = input("Enter student grade (A-F) = ").upper()
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
