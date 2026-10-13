
import test

print("=-=" * 20)
print("       CONTACT MANAGEMENT SYSTEM")
print("=-=" * 20)

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        test.add()
    elif choice == "2":
        test.show()
    elif choice == "3":
        test.search()
    elif choice == "4":
        test.delete()
    elif choice == "5":
        print("Thank you for using Contact Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
