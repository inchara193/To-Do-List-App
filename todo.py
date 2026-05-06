FILE = "tasks.txt"

# Load tasks
def load_tasks():
    try:
        with open(FILE, "r") as f:
            return f.readlines()
    except:
        return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        f.writelines(tasks)

# Add task
def add_task():
    task = input("Enter task: ") + "\n"
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

# View tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks")
    else:
        for i, t in enumerate(tasks):
            print(i, t.strip())

# Delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    index = int(input("Enter index to delete: "))
    
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Deleted!")
    else:
        print("Invalid index")

# Menu
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")