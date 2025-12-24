import json 
import os

#databse file to store data
DB_file = "cli_tasks.json"
#cli tasks.json means  to save command line tasks to json file  .json this is a extension that show file is in json format
def load_data():
    #load tasks from json file
    if not os.path.exists(DB_file):
        return []
    try:
        with open(DB_file, "r")as f:
            return json.load(f)
    except:
        return []

def  save_data(tasks):
    #save tasks to json file 
    with open(DB_file, "w")as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks = load_data()

    while True:
        print("\n ------------TO-D0- LIST--------------")
        print("1. View Tasks")
        print("2. Add task")
        print("3.Remove task")
        print("4.Exit")

        choice = input("choose an option 1-4: ")

        if choice == "1":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks found")
            for i,task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        
        elif choice == "2":
            new_task = input("Enter the task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_data(tasks)
                print("Task added successfully")
            else:
                print("Task cannot be empty")

        elif choice == "3":
            if not tasks:
                print("No tasks")
                continue
            try:
                task_num = int(input("Enter task number to remove:"))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num -1)
                    save_data(tasks)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("please give valid number")
                
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
        









            

    