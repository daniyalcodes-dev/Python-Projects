import string
import random
from colorama import Fore, Style ,init

def password_choice():
    while True:
        length = int(input("Enter length of password(minimum 6): "))
        if length >= 6:break
        print("Your password must be 6 character")

    choice1 = input("Include alphabets? (y/n): ").lower()
    while choice1 not in ('y', 'n'):
        choice1 = input("Please enter 'y' or 'n': ").lower()
    choice_alphabets = choice1 == "y"

    choice2 = input("Your password contain symbols (y/n): ").lower()
    while choice2 not in ('y', 'n'):
        choice1 = input("Please enter 'y' or 'n': ").lower()
    choice_symbols = choice2 == "y"

    generated_password = generator(length,choice_alphabets,choice_symbols)

    print(f"\nYour password is {generated_password}")
    
    with open("Password Generator/Record/Generated.txt", "a") as f:
        f.write(generated_password + "\n")

def check_choice():    
    password = input("Enter password: ")
    result = checker(password)

    with open(f"Password Generator/Record/Checked.txt", "a") as f:
        f.write(f"{password} ---- {result}\n")
    
    print(result)
 
def generated_password():
    print("All Generated passwords:")               
    try:
        with open("Record/Generated.txt") as f:
            password = f.readlines()
        if password:
            for p in password:
                print(p.strip())
        else:
            print("No generated passwords yet.")
    except FileNotFoundError:
        print("No generated passwords file found.")

def checked_password():
    print("All Checked password")

    try:
        with open(f"Password Generator/Record/Checked.txt") as f:        
            checked = f.readlines()
            if checked:
                for line in checked:
                    print(line.strip())
            else:
                print("No lines yet")
    except FileNotFoundError:
        print('No Checked password')


def generator(length,choice_alphabets,choice_symbols):   
    digits = string.digits
    character = digits

    if choice_alphabets:
        alphabets = string.ascii_letters
        character += alphabets

    if choice_symbols:
        symbols = string.punctuation
        character += symbols

    password = ''
    for _ in range(length):
        password += random.choice(character)

    return password

init(autoreset = True)
def checker(password):
    strength = 0    
    if len(password) >= 6:
        strength += 1

    if any(c.isupper() for c in password) or any(c.islower() for c in password):
        strength += 2
    
    
    if any(c.isdigit() for c in password):
        strength += 1
    
    if any(c in string.punctuation for c in password):
        strength += 1
    

    if strength <= 2:
        return f"{Fore.RED}Weak password{Style.RESET_ALL}"
    
    elif strength == 3 or strength == 4:
        return f"{Fore.YELLOW}Medium password{Style.RESET_ALL}"
    
    else:
        return f"{Fore.GREEN}Strong password{Style.RESET_ALL}"