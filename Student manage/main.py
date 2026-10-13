from functions import Student
  
                   
def main():

    student = Student()

    # ------ CLI interface ------

    while True:

        print("1. Add student")
        print("2. All Student")
        print("3. Update marks")
        print("4. Delete students")
        print("0. Exit")

        try:
            choice = int(input(">>> "))

            if choice == 1:
                name = input("Name: ")
                marks = float(input("Marks "))
                student.add_student(name,marks)

            elif choice == 2:
                student.show()

            elif choice == 3:
                name = input("Name: ")
                marks = float(input("Marks "))
                student.update_mark(name,marks)

            elif choice == 4:
                name = input("Name: ")
                student.delete_student(name)

            elif choice == 0:
                break

            else:
                raise ValueError
        
        except (ValueError,TypeError) as v:
            print("Error",v)


if __name__ == "__main__":
    main()