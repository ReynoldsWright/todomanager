from storage import save_tasks, load_tasks

def add_task(tasks):
    newtask = input("What is the new task? ")
    newentry = {"name": newtask, "status": "Incomplete"} # Key matches!
    tasks.append(newentry)
    print(f"Successfully added: {newtask}")

def list_tasks(tasks):
    print("\n--- Your Current Hierarchy of Tasks ---")
    for i, task in enumerate(tasks, 1):
        # We use task['name'] because that is the key in our dictionary
        print(f"{i}. {task['name']} | Status: {task['status']}")

def mark_task_done(tasks):
    list_tasks(tasks)
    choice = int(input('\nEnter the number of the task you finished: '))
    index = choice - 1
    # Check if index is valid so it doesn't crash
    if 0 <= index < len(tasks):
        tasks[index]["status"] = "Done ✅"
        print('Hierarchy updated. Progress logged.')
    else:
        print("Invalid number!")
     
def remove_task(tasks):
    list_tasks(tasks)
    try:
        choice = int(input('\nEnter the number of the task to remove: '))
        index = choice - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("task removed succusfully")
        else:
         print("invalid number!")
    except ValueError:
        print("please enter a valid number")


def main():

    tasks = load_tasks()

    print("--- Welcome to To-Do Manager ---")

    while True:
        print("\n[A]dd Task | [L]ist Tasks | [M]ark Done | [R]emove | [E]xit")
        choice = input("Select an option: ").lower()
        if choice == 'a':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == 'l': 
            list_tasks(tasks)
        elif choice == 'm':
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == 'r':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == 'e':
            print('Leaving To-Do Manager, Goodbye.')
            break
        else:
            print('Invalid command, try again.')


if __name__ == "__main__":
    main()