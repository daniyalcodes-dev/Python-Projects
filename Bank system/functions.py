from datetime import datetime, timedelta
import os
import json


class Account:
    def __init__(self, name, account_number, pin, balance=0,lock_until=None):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.created_at = datetime.now().strftime("%B %d, %Y")
        self.lock_until = lock_until


    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError
        self.balance  += amount

    def transfer(self,recieving_user,amount):
        self.withdraw(amount)
        recieving_user.deposit(amount)

    def to_dict(self):
        return{
            "Name" : self.name,
            "Account Number" : self.account_number,
            "Pin" : self.pin,
            "Balance": self.balance,
            "Date": self.created_at,
            "Lock Until": self.lock_until
        }

    def __str__(self):
        return f"[{self.account_number} {self.name} Balence - {self.balance:.2f}]"


class Bank:
    file = "File.json"
    def __init__(self):
        self.accounts = {}
        self.load()


    def load(self):
        if os.path.exists(self.file):
            try:
                with open(self.file, "r") as file:
                    data = json.load(file)

                for k, v in data.items():
                    self.accounts[k] = Account(v["Name"],v["Account Number"],v["Pin"],v["Balance"],v.get("Lock Until"))

            except json.JSONDecodeError:
                print("Error: JSON file is empty or invalid.")

    def save(self):
        with open(self.file,"w") as file:
            json.dump(
                {k : v.to_dict() for k,v in self.accounts.items()},file,indent=2
            )

    def create_account(self,name,pin):
        account_number = str(1000000001 + len(self.accounts))
        user_account = Account(name,account_number,pin)
        self.accounts[account_number] = user_account
        self.save()
        print(f"Dear {name} \nYour account has created. Your account number is {account_number}")

    
    def get_user(self,account_number):
        user = self.accounts.get(account_number)
        if user:
            return user
        print("User is no available")
        return False

    def check_pin(self, account_number):
        account = self.get_user(account_number)

        if not account:
            return False

        if account.lock_until:
            unlock_time = datetime.fromisoformat(account.lock_until)

            if datetime.now() < unlock_time:
                remaining = unlock_time - datetime.now()
                hours = int(remaining.total_seconds() // 3600)
                minutes = int((remaining.total_seconds() % 3600) // 60)

                print(f"Account locked! Try again in {hours}h {minutes}m.")
                return False

            account.lock_until = None
            self.save()

        for attempt in range(3):
            pin = input("Enter your PIN: ")

            if str(account.pin) == str(pin):
                print("PIN verified successfully!")
                return True

            remaining = 2 - attempt

            if remaining:
                print(f"Wrong PIN! {remaining} attempts remaining.")

        account.lock_until = (
            datetime.now() + timedelta(hours=24)
        ).isoformat()

        self.save()
        print("Too many attempts! Account locked for 24 hours.")
        return False
    
    def deposit_amount(self,account_number,deposit_amount):
        user = self.get_user(account_number)
        if self.check_pin(account_number):
            user.deposit(deposit_amount)
            self.save()
            print(f"Deposit: {deposit_amount} \nNew balance: {user.balance:.2f}")

        
    def withdraw_amount(self,account_number,withdraw_amount):
        user = self.get_user(account_number)
        if self.check_pin(account_number):
            user.withdraw(withdraw_amount)
            self.save()
            print(f"Deposit: {withdraw_amount} \nNew balance: {user.balance:.2f}")

    def transfer_amount(self, sender, receiver, amount):
        sending_user = self.get_user(sender)
        receiving_user = self.get_user(receiver)

        if not sending_user or not receiving_user:
            return

        if not self.check_pin(sender):
            return

        try:
            sending_user.transfer(receiving_user, amount)
            self.save()
            print(f"Transfer successful: {amount}")
            print(f"New balance: {sending_user.balance:.2f}")
        except ValueError as error:
            print(error)
        
    def details(self,account_number):
        user = self.get_user(account_number)
        print(user)
    