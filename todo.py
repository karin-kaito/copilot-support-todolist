# todo-list
import sys

class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
        else:
            print("Invalid task number.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def main():
    todo = ToDo()
    while True:
        print("\nToDo List:")
        todo.display_tasks()
        print("\nCommands:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(task_number)
        elif choice == '3':
            todo.display_tasks()
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
