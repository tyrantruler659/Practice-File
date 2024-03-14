tasks = []

def addtask():
    task = input("Please enter your task")
    tasks.append(task)
    print(f"your task '{task}' has been added to the list")

def deletetask():
    tasklist()

    try:
        task_to_delete = int(input("Enter the task # to delete"))
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            removedTask = tasks.pop(task_to_delete)
            print(f"task {task_to_delete} has been removed")

        else:
            print(f"Task # '{task_to_delete}' not found")
    except:
        print("Invalid Number")

def tasklist():
    if not tasks:
        print("There are no tasks rightnow")
    
    else:
        print("current tasks")
        for index, task in enumerate(task):
            print(f" task #{index}. {task}" )
    
    


if __name__ == "__main__":
    while True:
        print("Welcome here, We hope you find it useful.")
        print("n/")
        print("1. Add a task")
        print("2. Delete a Task")
        print("3. List Task")
        print("4. Quit")

        choice = input("What would you like to do?")

        if(choice == "1"):
            addtask()
        elif(choice == "2"):
            deletetask()
        elif(choice == "3"):
            tasklist()
        elif(choice == "4"):
            print("exiting the program")
            break

        else:
            print("Invalid Input. Please Try Again.")
    

