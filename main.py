import json
import os
import datetime

FILENAME = "tasks.json"
tasks = []

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
add_task(tasks)
def view_task():
    if not tasks:
        print("The list is empty")
    print("-"*100)
    print(f"{'ID':10} {'Title':25} {'Priority':25} {'Due Date':25} {'Completed':25}")
    print("-"*100)
    for index, task in enumerate(tasks, 1):
        print(f"{str(index):10} {task['title']:25} {task['priority']:25} {task['due_date']:25} {task['completed']:25}")
view_task()