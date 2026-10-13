# This is simple to-do list

tasks = []

def main():
    print("=-=" * 12)
    print("-=-" * 12)
    print("TO-DO List")
    print("-=-" * 12)
    print("=-=" * 12)

    tasks = load()

    while True:
        user = input(
            "Please enter your choice\n"
            "1. Add task\n"
            "2. Show task\n"
            "3. Delete task\n"
            "0. Exit\n"
            ">>> "
        )

        if user == "0":
            break
        elif user == "1":
            add_task(tasks)
        elif user == "2":
            show_task(tasks)
        elif user == "3":
            rm_task(tasks)
        else:
            print("Please enter a valid number.\n")


def load():
    try:
        with open("To-do list.txt") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
    
def save(tasks):
    with open("To-do list.txt","w") as file:
        for task in tasks:
            file.write(f"{task}\n")

 
def add_task(tasks):
    user = input("Enter the task: ")
    tasks.append(user)
    save(tasks)

def show_task(tasks):
    if len(tasks) == 0:
        print("No tasks added!")
    else:
        for no in range(len(tasks)):
            print(f"{no + 1} : {tasks[no]}")
   
def rm_task(tasks):
    if len(tasks) == 0:
        print("No tasks added!")
    else:
        show_task(tasks)
        try:
            num = int(input("Enter the Choice(number)>>> "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                save(tasks)
                print("Task deleted")

            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter a number")

            
if __name__ == "__main__":  
    main()