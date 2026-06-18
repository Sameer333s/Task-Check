tasks = []
completed = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Quit from here")
    
    choice = input("Pick an option (1-5): ")

    if choice == '1':
        if len(tasks) == 0:
            print("Your list is completely empty.")
        else:
            print("\nHere are your tasks:")
            for i in range(len(tasks)):
                if completed[i] == True:
                    box = "[x]"
                else:
                    box = "[ ]"
                print(str(i + 1) + ". " + box + " " + tasks[i])

    elif choice == '2':
        new_task = input("What's the task? ")
        if new_task == "":
            print("Task name can't be blank.")
        else:
            tasks.append(new_task)
            completed.append(False)
            print("'" + new_task + "' added to the list!")

    elif choice == '3':
        if len(tasks) == 0:
            print("Nothing to complete yet!")
        else:
            for i in range(len(tasks)):
                if completed[i] == True:
                    box = "[x]"
                else:
                    box = "[ ]"
                print(str(i + 1) + ". " + box + " " + tasks[i])
            
            num_input = input("Enter the task number you finished: ")
            if num_input.isdigit():
                num = int(num_input)
                if num >= 1 and num <= len(tasks):
                    completed[num - 1] = True
                    print("Nice job! Task marked as done.")
                else:
                    print("That number isn't on the list.")
            else:
                print("Oops, please enter a valid number.")

    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                if completed[i] == True:
                    box = "[x]"
                else:
                    box = "[ ]"
                print(str(i + 1) + ". " + box + " " + tasks[i])
            
            num_input = input("Enter the task number to delete: ")
            if num_input.isdigit():
                num = int(num_input)
                if num >= 1 and num <= len(tasks):
                    idx = num - 1
                    deleted_item = tasks[idx]
                    tasks.pop(idx)
                    completed.pop(idx)
                    print("Deleted '" + deleted_item + "' from the list.")
                else:
                    print("That number isn't on the list.")
            else:
                print("Oops, please enter a valid number.")

    elif choice == '5':
        print("Catch you later!")
        break

    else:
        print("Invalid choice, try entering a number between 1 and 5.")