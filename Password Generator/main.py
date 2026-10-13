
import os
import func

if not os.path.exists("Password Generator/Record"):
    os.makedirs("Password Generator/Record")


print("="*40)
print('\t\tPASS MASTER')
print("="*40)

while True:
    print("\n" + "_"*40)
    print("MENU OPTIONS:")
    print("1. Generate password")
    print("2. Check strength")
    print("3. Show generated passwords")
    print("4. Show checked passwords")
    print("0. Exit")
    print("="*40)
    
    try:
        choice = int(input('\nEnter your choice: '))
        if choice == 0:
            break

        if choice == 1:func.password_choice()
        elif choice == 2:func.check_choice()
        elif choice == 3:func.generated_password()
        elif choice == 4:func.checked_password()
        else:
            print("Enter number 0-4")

    except ValueError:
        print("Enter valid choice")