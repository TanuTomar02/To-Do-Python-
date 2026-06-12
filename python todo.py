def main():
    # Initialize the storage list
    my_tasks = []

    while True:
        # 1. INPUT (Data Entry)
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        # 2. PROCESS (Logic/Modification)
        if choice == '1':
            task = input("Enter the task: ")
            my_tasks.append(task)  # Appending to the end of the list[span_1](end_span)
            print(f"Task '{task}' added!")
            
        elif choice == '2':
            # 3. OUTPUT (Display/View)
            print("\nYour Tasks:")
        
            for index, task in enumerate(my_tasks, start=1):
                print(f"{index}. {task}")
                
        elif choice == '3':
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()