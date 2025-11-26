class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added."

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' removed."
        else:
            return f"Task '{task}' not found."

    def list_tasks(self):
        # Returns a list of strings for easy display/testing
        return [f"{idx}. {task}" for idx, task in enumerate(self.tasks, start=1)]

def main():
    todo_app = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            print(todo_app.add_task(task))
        elif choice == '2':
            task = input("Enter the task to remove: ")
            print(todo_app.remove_task(task))
        elif choice == '3':
            print("Tasks:")
            for item in todo_app.list_tasks():
                print(item)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()