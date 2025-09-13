#Simple To-Do List Manager

tasks = []
                
while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add task
        # your code here
        task = input("Input Your Task: ")
        tasks.append(task)
        print(f"'{task}' Task!")

    elif choice == "2":

        if not tasks:
            print("No Task Available")
        else:
            print("\nYour Task:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        # Remove task
        # your code here
        if not tasks:
            print("No task remove!")
        else:
            print("Your Task:")
            for i, task in enumerate(tasks, start=1):
               print(f"{i}. {task}")
        try:
                task_enum = int(input("Enter task number to remove: "))
                if 1 <= task_enum <= len(tasks):
                    removed = tasks.pop(task_enum - 1)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number.")
        except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")
