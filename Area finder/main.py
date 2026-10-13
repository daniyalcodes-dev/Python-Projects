from shapes import functions

#  ------ CLI interface ------

print("="*41)
print("             AREA FINDER")
print("="*41)

#   -----------MENU----------  #

print("\n\nYou can find area of any of these")
print("\n1. Circle\n2. Square\n3. Triangle\n4. Rectangle\n5. Parallelogram\n6. Trapezium\n7. Rhombus\n8. Ellipse\n0. Exit\n")

#   -----------MAIN LOOP----------  #
while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Thanks for using this program!\n")
            break

        elif choice == 1:functions.circle()
        elif choice == 2:functions.square()
        elif choice == 3:functions.triangle()
        elif choice == 4:functions.rectangle()
        elif choice == 5:functions.parallelogram()
        elif choice == 6:functions.trapezium()    
        elif choice == 7:functions.rhombus()
        elif choice == 8:functions.ellipse()
        else:
            print("Invalid choice! Please enter 0, 1, 2, 3,...,8\n")
    except:
        print("Invalid choice! Please enter a number between 0 to 8 \n")