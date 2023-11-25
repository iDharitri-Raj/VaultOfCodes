# Function to add a task to the to-do list
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully.")

# Function to delete a task from the to-do list


def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")

# Function to display the to-do list


def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to mark a task as complete


def mark_complete(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = f"{tasks[task_index - 1]} (Completed)"
        print("Task marked as complete.")
    else:
        print("Invalid task index.")

# Main function to run the to-do list application


def main():
    tasks = []

    while True:
        print("\n====To-Do List Application====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            task_index = int(
                input("Enter the task index to mark as complete: "))
            mark_complete(tasks, task_index)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
