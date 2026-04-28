#imitialising dictonary
student_grades = {}

#add a new student
def add_student(name, grade):
    student_grades[name] = grade
    #eg [sagar] = 100
    print(f"Added {name} with a {grade}")
    #eg added sagar with a 100

#update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        #eg sagar = 200
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")

#function with delet student
def delet_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been sucessfully deleted")

    else:
        print(f"{name} is not found!")

#function to view students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    
    else:
        print("No student found/added")

display_all_students()

def main():
    while True:
        print('\n Sytudent Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)
        
        elif choice ==2:
            name = input("Enter student name = ")
            grade = int(input("Enter student name = "))
            update_student(name,grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delet_student(name)

        elif choice == 4:
            display_all_students()
        
        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")

if __name__ =='__main__':
    main()