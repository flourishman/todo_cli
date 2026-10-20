import json
import os
import datetime


FILENAME = "tasks.json"
#tasks = []
def save_file(tasks):
    try:
        with open(FILENAME, 'w') as file:
            json.dump(tasks, file, indent=4)
            print("File save successfully")
    except OSError:
        print("Error occur. please try again")
        
def load_file():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, 'r') as file:
           return json.load(file)
    except json.JSONDecodeError:
        return []
      
def add_task(tasks):
    title = input("Enter title of the task: ").strip()
    
    while True:
        priority = input("Enter priority 'High' or 'Medium' or 'Low' ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid entering, please enter 'High', 'Medium', 'Low'")
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    
    new_task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    
    tasks.append(new_task)
    
    save_file(tasks)
    
#add_task(tasks)

def view_task(tasks):
    if not tasks:
        print("The list is empty")
        return
    print("-"*100)
    print(f"{'ID':10} {'Title':25} {'Priority':25} {'Due Date':25} {'Completed':25}")
    print("-"*100)
    for index, task in enumerate(tasks, 1):
        status = "Completed [X]" if task['completed'] else "Pending []"
        print(f"{str(index):10} {task['title']:25} {task['priority']:25} {task['due_date']:25} {status:25}")
#view_task(tasks)

def complete_task(tasks):
    if not tasks:
        print("The list is empty")
        return
    
    view_task(tasks)
    
    while True:
            try:
                task_id = int(
                    input("Enter the ID number of the task to mark complete: ").strip()
                )
                if 1 <= task_id <= len(tasks):
                    # Update the task's completed status to True
                    tasks[task_id - 1]["completed"] = True
                    print(f"Task '{tasks[task_id - 1]['title']}' marked as completed!")

                    # Save the updated list to JSON
                    save_file(tasks)
                    break
                else:
                    print(f"Please enter a number between 1 and {len(tasks)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
def main():
   tasks = load_file()
   
   while True:
        print("\n-----Welcome to your todo app-----")
        
        choice_opt = [
            "1. Add Task: ",
            "2. View Tasks: ",
            "3. Complete Task:",
            "4. Exit: ",    
        ]
        
        for choice in choice_opt:
            print(choice)
        
        user_choice = input("Select your choice ").strip()
        if user_choice == "1":
            add_task(tasks)
        elif user_choice == "2":
            view_task(tasks)
        elif user_choice == "3":
            complete_task(tasks)
        elif user_choice == "4":
            print("Done! Thank you")
            break
        else:
            print("Invalid choice, try again later")
            
        
if __name__ == "__main__":
    main()