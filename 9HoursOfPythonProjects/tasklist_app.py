
def main():
    tasks = []

    while True:
        view_options()
        user_choice = input("Select OPTION: ")

        if user_choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task added.")

        elif user_choice == "2":
            view_tasks(tasks)
            task = input("Type or Select task to be deleted: ")

            if task in tasks:
                tasks.remove(task)
                print("Task found and deleted - via text")

            elif task.isdigit():
                #task in range(len(tasks)):
                task = int(task) - 1
                if task in range(len(tasks)):
                    tasks.remove(tasks[task])
                    print("Task found and deleted - via index")
                else:
                     print("Task not found - out-of-range selection. Try again.")

            else:
                print("task not found. Try again.")

        elif user_choice == "3":
            view_tasks(tasks)

        elif user_choice == "9":
             print("Closing App....")
             break
        
        else:
             print("Invalid input. Try again.")
             print()
             continue

        print()


def view_options():
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print()
    print("9. Close App")


def view_tasks(tasks: list):
    for i, each_task in enumerate(tasks):
                print(f"{i + 1}) {each_task}")
                print()


if __name__ == "__main__":
    main()