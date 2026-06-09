def add_student():

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + roll_no + "," + course + "\n")

    print("Student Added Successfully!")


def view_students():

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if len(students) == 0:
            print("No Students Found")
            return

        print("\n------ ALL STUDENTS ------")

        count = 1

        for student in students:

            data = student.strip().split(",")

            print(f"\nStudent {count}")
            print(f"Name: {data[0]}")
            print(f"Roll No: {data[1]}")
            print(f"Course: {data[2]}")

            count += 1

    except FileNotFoundError:
        print("No Student File Found")


def total_students():

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        print("\nTotal Students:", len(students))

    except FileNotFoundError:
        print("No Students Found")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Total Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        total_students()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
