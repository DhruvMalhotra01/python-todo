todo_list = []

while True:
    # Display menu options
    print("\n===== TO-DO List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.append({'task': task, 'completed': False})
        print(f"Task '{task}' added to the to-do list.")

    elif choice == '2':
        if not todo_list:
            print("No tasks in the to-do list.")
        else:
            print("\n===== Tasks in To-Do List =====")
            for index, todo in enumerate(todo_list, start=1):
                status = "Completed" if todo['completed'] else "Not Completed"
                print(f"{index}. {todo['task']} - {status}")

    elif choice == '3':
        if not todo_list:
            print("No tasks in the to-do list.")
        else:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]['completed'] = True
                print(f"Task '{todo_list[task_number - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == '4':
        confirmation = input("Are you sure you want to clear all tasks? (yes/no): ")
        if confirmation.lower() == 'yes':
            todo_list = []
            print("All tasks cleared.")
        else:
            print("Clear operation cancelled.")

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")