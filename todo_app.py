tasks = []


while True:
    print("To-Do List: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("\nOptions:" )
    print("1. Add Task" )
    print("2. Remove Task" )
    print("3. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append(task_name)
        print("Task added!")
    elif choice == "2":
        task_index = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
        else: 
            print("Invalid task number.")
    elif choice == "3":
        print("Existing...")
        break
    else:
         print("Invalid choice. Please select a valid option.")
