import json
def load():
    try:
        with open("contacts.json",encoding="utf-8") as file:
            return json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        return []

def save(contact):
    with open("contacts.json","w") as file:
        json.dump(contact,file)

def add():
    name = input("Enter your name: ").strip().lower()
    contact_no = input("Contact Number: ").strip()
    while len(contact_no) != 11 or not(contact_no.startswith("03")) or not contact_no.isdigit():
        print("Please Enter a Valid Number")
        contact_no = input("Contact Number: ").strip()
    email = input("Email: ").strip()
    while not email.endswith("@gmail.com") or any(c["Email"].lower() == email for c in contact):
        if any(c["Email"].lower() == email for c in contact):
            print("Email already exists!")
        else:
            print("Invalid email!")

        email = input("Email: ").strip().lower()

    contact.append({"Name":name,"Contact number" : contact_no ,"Email": email  })
    save(contact)

contact = load()
        
def show():
    if len(contact) == 0:
            print("There is no added user")
    for i in contact:
        print(f"Name: {i['Name']}\nContact Number : {i['Contact number']}\nEmail: {i['Email']} ")
    
        
def search():
    user = input("Enter name for search: ").strip().lower()
    found = False
    for i in contact:
        if user in i['Name'].lower():
            print(f"Name: {i['Name']}\nContact Number : {i['Contact number']}\nEmail: {i['Email']} ")
            found = True

    if not found:
        ("This user is not available")
        
        

def delete():
    name = input("Email: ").lower()
    
    for i in contact:
        if i["Email"].lower() == name:
            contact.remove(i)
            save(contact)
            print("Data is deleted!")
            return    
        
    print("USER NOT FOUND")



