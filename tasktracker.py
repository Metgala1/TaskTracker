import datetime
import json
import os
import sys

FILE_NAME = "task.json"

#Create JSON file if it doesnt exist
if not os.path.exists(FILE_NAME):
     with open(FILE_NAME , "w") as file:
          json.dump([], file)

#Load tasks
def loadTask():
     with open(FILE_NAME, "r") as file:
          return json.load(file)

tasks = loadTask()

#Save tasks
def saveTasks():
     with open(FILE_NAME, "w") as file:
          json.dump(tasks, file, indent=4)

def generateId():
     if len(tasks) == 0:
          return 1
     else:
          return max(task["id"] for task in tasks) + 1
          

print(" == Task Tracker == ")


def addTask():
        if len(sys.argv) < 4:
             print("Usage: python task_tracker.py add <Task Name> <Description>")
             return
        task_name = sys.argv[2]
        description = sys.argv[3]

        myTask = {
             "id": generateId(),
             "name": task_name ,
             "description": description,
             "status": "todo",
             "createdAt": datetime.datetime.now().isoformat(),
             "updatedAt": datetime.datetime.now().isoformat()
        }

        tasks.append(myTask)
        saveTasks()
        print("Tasked added successfully!")
             
             

def updateTask(id):
     task_to_update = None

     for task in tasks:
          if task["id"] == id:
               task_to_update = task
               break
     if task_to_update is None:
          print("Task is not found")
          return
     if len(sys.argv) < 5:
          print("Usage: python task_tracker.py add <Task Name> <Description>")
          return
     task_to_update["name"] = sys.argv[3]
     task_to_update["description"] = sys.argv[4]
     task_to_update["updatedAt"] = datetime.datetime.now().isoformat()

     saveTasks()
     print("Task updated successfully!")
          

def deleteTask(id):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            saveTasks()
            print(f"Task with ID {id} deleted!")
            return
    

def displayTask():
     if len(tasks) == 0:
          print("No tasks available.")
          return
     
     for task in tasks:
          print("----------------------------")
          print(f"ID: {task['id']}")
          print(f"Name: {task['name']}")
          print(f"Description: {task['description']}")
          print(f"Status: {task['status']}")
          print(f"Created: {task['createdAt']}")
          print(f"Updated: {task['updatedAt']}")

def markInProgress(id):
    for task in tasks:
        if task["id"] == id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.now().isoformat()
            saveTasks()
            print("Task marked as in-progress.")
            return

    print("Task not found!")

def markDone(id):
    for task in tasks:
        if task["id"] == id:
            task["status"] = "done"
            task["updatedAt"] = datetime.datetime.now().isoformat()
            saveTasks()
            print("Task marked as done.")
            return

    print("Task not found!")

def doneTask():
    if not any(task["status"] == "done" for task in tasks):
        print("You have no task with the status 'Done'")
        return
    doneTasks = [task for task in tasks if task["status"] == "done"]
    for task in doneTasks:
        print(f"ID: {task['id']} , {task['name']}")

def todoTask():
     if not any(task["status"] == "todo" for task in tasks):
          print("You have no task with status of 'Todo'")
          return
     todoTask = [task for task in tasks if task["status"] == "todo"]
     for task in todoTask:
          print(f"ID: {task["id"]} , {task["name"]}")

def inProgressTask():
     if not any(task["status"] for task in tasks):
          print("You have no tasks with the status of 'In-progress'")
          return
     inProgressTask = [task for task in tasks if task["status"] == "in-progress"]
     for task in inProgressTask:
          print(f"ID: {task["id"]} , {task["name"]}")



               

if len(sys.argv) < 2:
     print("""
Task Tracker Commands

python3 tasktracker.py add "Task Name" "Description"
python3 tasktracker.py update 1 "New Name" "New Description"
python3 tasktracker.py delete 1
python3 tasktracker.py list
python3 tasktracker.py mark-in-progress 1
python3 tasktracker.py mark-done 1
python3 tasktracker.py done
python3 tasktracker.py todo
python3 tasktracker.py in-progress

""")
     sys.exit()
     
commamd = sys.argv[1]

try:
     match commamd:
          case "add":
               addTask()
          case "list":
               displayTask()
          case "update":
               updateTask(int(sys.argv[2]))
          case "delete":
               deleteTask(int(sys.argv[2]))
          case "mark-in-progress":
               markInProgress(int(sys.argv[2]))
          case "mark-done":
               markDone(int(sys.argv[2]))
          case "done":
               doneTask()
          case "todo":
               todoTask()
          case "in-progress":
               inProgressTask()
          case _:
               print("Unkwon command.")
except ValueError:
     print("ID must be a number")
except IndexError:
     print("Missing command arguments.")
          
     
          