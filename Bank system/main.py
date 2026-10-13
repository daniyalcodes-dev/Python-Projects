from functions import Bank

bank = Bank()


def main():
    while True:
        print("\n" + "=-=" * 12)
        print("       BANK MANAGEMENT SYSTEM")
        print("=-=" * 12)
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Account Details")
        print("6. Exit")
        print("=-=" * 12)

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter your name: ").strip()
                pin = input("Create your PIN: ").strip()

                if not name or not pin:
                    print("Name and PIN cannot be empty!")
                    continue

                bank.create_account(name, pin)

            elif choice == "2":
                account_number = input("Enter account number: ").strip()
                amount = float(input("Enter deposit amount: "))

                bank.deposit_amount(account_number, amount)

            elif choice == "3":
                account_number = input("Enter account number: ").strip()
                amount = float(input("Enter withdrawal amount: "))

                bank.withdraw_amount(account_number, amount)

            elif choice == "4":
                sender = input("Enter your account number: ").strip()
                receiver = input("Enter receiver account number: ").strip()
                amount = float(input("Enter transfer amount: "))

                bank.transfer_amount(sender, receiver, amount)
                bank.save()
                print("Transfer completed successfully!")

            elif choice == "5":
                account_number = input("Enter account number: ").strip()

                if bank.get_user(account_number):
                    if bank.check_pin(account_number):
                        bank.details(account_number)

            elif choice == "6":
                print("Thank you for using our banking system!")
                break

            else:
                print("Invalid choice! Select 1 to 6.")

        except ValueError as error:
            print(f"Invalid input: {error}")

        except (OSError, TypeError, KeyError) as error:
            print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()