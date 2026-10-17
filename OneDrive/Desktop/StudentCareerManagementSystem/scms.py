# Student Career Management System

students = []


def add_student():
    print("\n--- Add Student Details ---")

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA (out of 10): "))
    skills = input("Enter skills separated by commas: ")
    career_goal = input("Enter career goal: ")

    student = {
        "name": name,
        "roll_number": roll_number,
        "branch": branch,
        "cgpa": cgpa,
        "skills": skills,
        "career_goal": career_goal
    }

    students.append(student)

    print("\nStudent details added successfully!")


def view_students():
    print("\n--- Student Career Details ---")

    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            print("\nName:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Branch:", student["branch"])
            print("CGPA:", student["cgpa"])
            print("Skills:", student["skills"])
            print("Career Goal:", student["career_goal"])


def check_eligibility():
    print("\n--- Placement Eligibility Check ---")

    roll_number = input("Enter roll number: ")

    found = False

    for student in students:
        if student["roll_number"] == roll_number:
            found = True

            print("Student Name:", student["name"])
            print("CGPA:", student["cgpa"])

            if student["cgpa"] >= 7.0:
                print("Status: Eligible based on the project's CGPA criterion.")
            else:
                print("Status: Not eligible based on the project's CGPA criterion.")

            print("Note: Actual company eligibility criteria may differ.")
            break

    if not found:
        print("Student record not found.")


def search_student():
    print("\n--- Search Student ---")

    roll_number = input("Enter roll number: ")

    found = False

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("CGPA:", student["cgpa"])
            print("Skills:", student["skills"])
            print("Career Goal:", student["career_goal"])

            found = True
            break

    if not found:
        print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT CAREER MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Check Placement Eligibility")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            check_eligibility()

        elif choice == "4":
            search_student()

        elif choice == "5":
            print("Thank you for using the Student Career Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()