def add_task(tasks):
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- Your To-Do List ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
   
    my_tasks = []

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            print("Thank you for using the To-Do List!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
