def todo_manager():
    tasks = [
        {"name": "Learn Gitbasics", "status": "Incomplete"},
        {"name": "GitHub Upload", "status": "Incomplete"},
        {"name": "Cooldown", "status": "Incomplete"}
    ]

    print("--- Welcome to To-Do Manager ---")

    while True:
        print("\n[A]dd | [L]ist | [M]ark Done | [E]xit")
        choice = input("Choose: ").lower()

        if choice == 'a':
            newtask = input("New task: ")
            tasks.append({"name": newtask, "status": "Incomplete"})
            print("Added.")

        elif choice == 'l':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['name']} | {task['status']}")

        elif choice == 'm':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['name']} | {task['status']}")
            index = int(input("Task number: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["status"] = "Done"
                print("Updated.")
            else:
                print("Invalid.")

        elif choice == 'e':
            break

        else:
            print("Invalid option.")

todo_manager()

