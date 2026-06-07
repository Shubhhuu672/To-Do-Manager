import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    tasks = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split("|")

            if len(data) == 2:
                tasks.append({
                    "task": data[0],
                    "completed": data[1] == "True"
                })

    return tasks

def save_tasks(tasks):

    with open(FILE_NAME, "w") as file:

        for task in tasks:
            file.write(
                f"{task['task']}|{task['completed']}\n"
            )

def add_task(tasks):

    task = input("Enter Task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)

    print("Task Added!")

def view_tasks(tasks):

    if not tasks:
        print("No Tasks Found!")
        return

    print("\n===== TASKS =====")

    for i, task in enumerate(tasks, start=1):

        status = "Done" if task["completed"] else "Pending"

        print(
            f"{i}. {task['task']} - {status}"
        )

def complete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    num = int(input("Task Number: ")) - 1

    if 0 <= num < len(tasks):

        tasks[num]["completed"] = True

        save_tasks(tasks)

        print("Task Completed!")

def delete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    num = int(input("Task Number: ")) - 1

    if 0 <= num < len(tasks):

        removed = tasks.pop(num)

        save_tasks(tasks)

        print(
            f"Deleted: {removed['task']}"
        )

def main():

    tasks = load_tasks()

    while True:

        print("\n===== TO-DO MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()