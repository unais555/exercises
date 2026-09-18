import json


def add_student():
    with open("students.json", "r") as file:
        students = json.load(file)
    student_id = input("Student ID : ")
    name = input("Enter name : ")
    age = input("Enter age : ")
    course = input("Enter course : ")
    student = {
        "student_id" : student_id,
        "name" : name,
        "age" : age,
        "course" : course 
    }
    students.append(student)
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Student Added Successfully!")


def view_student():
    with open("students.json", "r") as file:
        students = json.load(file)
    if not students:
        print("Empty")
    else:
        for student in students:
            print("********************")
            print("Student ID : ",student["student_id"])
            print("Name : ", student["name"])
            print("Age : ", student["age"])
            print("Course : ", student["course"])
            print("********************")


def update_student():
    student_id_toupdate = input("Enter Student ID : ")
    with open("students.json", "r") as file:
        students = json.load(file)
    
    for student in students:
        if student["student_id"] == student_id_toupdate:
            student["name"] = input("Enter name : ")
            student["age"] = input("Enter age : ")
            student["course"] = input("Enter course : ")

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)
            print("Updated Successfully")
            return 
    print("Invalid student ID")



def delete_student():
    student_todelete = input("Enter Student ID : ")
    with open("students.json", "r") as file:
        students = json.load(file)
    for student in students:
        if student["student_id"] == student_todelete:
            students.remove(student)
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)
            print("Deleted Successfully")
            return 



while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")