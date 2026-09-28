print("Welcome to my Task Manager...")


tasks = []

while True:
    print("[Task manager]")

    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. exit")
    choice = int(input("Enter your choice"))

    if choice == 1:
        task = input("Enter your task").lower()
        tasks.append(task)
        print(tasks)
    if choice == 2:
        print(tasks)
    if choice == 3:
        user = int(input("Choice the task you want to delete :"))
        tasks.remove(user)
    if choice == 4 :
        tasks.index(tasks,"done")
    if choice == 5:
        break

    







