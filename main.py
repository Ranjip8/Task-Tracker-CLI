


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
        for index, task in enumerate(tasks, 1):
            print (f"{index},{task})")
        
        print(tasks)
    if choice == 2:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    if choice == 3:
        user = int(input("Choice the task you want to delete :"))
        tasks.remove(tasks[user - 1])
    else:
        print("Invalid choice")
        print(tasks)
    if choice == 4 :
        user = int(input("Choice the task you want to mark as done :"))
        if user < 1 or user > len(tasks):
            print("Invalid task number")
        else:
         tasks[user - 1] = tasks[user - 1] + "(Your task is done)"
        
    if choice == 5:
        break
    
    







