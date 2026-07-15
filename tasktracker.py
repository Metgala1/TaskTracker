import datetime
import json
import os
import sys

FILE_NAME = "task.json"

#Create JSON file if it doesnt exist
if not os.path.exists(FILE_NAME):
     with open(FILE_NAME , "w") as file:
          json.dump([], file)

print(" == Task Tracker ==")
tasks = [{"id": 0 , "name": "Play Game" , "description": "Beat Richy" , "status": "todo" , "createdAt": datetime.datetime.now() , "updatedAt": datetime.datetime.now()},
         {"id": 1 , "name": "Go to church" , "description": "Pray to Good" , "status": "in-progress" , "createdAt": datetime.datetime.now() , "updatedAt": datetime.datetime.now()}
         ]


def addTask():
        task_name = input("Enter Task Name: ")
        description = input("Describe Task: ")
        status = "todo"
        createdAt = datetime.datetime.now()
        updateAt = datetime.datetime.now()
        id = 2

        myTask = {}
        myTask["id"] = id
        myTask["name"] = task_name
        myTask["description"] = description
        myTask["status"] = status
        myTask["createdAt"] = createdAt
        myTask["updatedAt"] = updateAt
        
        tasks.append(myTask)
        id += 1

def updateTask(id):
     task_to_update = {}
     for task in tasks:
          if task["id"] == id:
               task_to_update = task
     print("Updating task: ", task_to_update["id"])
     print("Current task name: ", task_to_update["name"])
     print("Current task description: ", task_to_update["description"])

     new_name = input("Edit name: ")
     new_description = input("Enter new description")
     status = input("Update status: ")
     updated_time = datetime.datetime.now()

     task_to_update["name"] = new_name
     task_to_update["description"] = new_description
     task_to_update["status"] = status
     task_to_update["updateAt"] = updated_time

def deleteTask(id):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            print(f"Task with ID {id} deleted!")
            return

def displayTask():
     num = 1
     for task in tasks:
          print(f"{num}. Name: {task["name"]}, Id: {task["id"]}")
          num += 1

while True:
    print()
    print("Select 1 to add Task")
    print("Select 2 to View Tasks")
    print("Select 3 to Update Task")
    print("Select 4 to Delete Task ")
    print("Select 5 to Exit Programm")
    print()

    operation = int(input("Choose operation: "))
    match operation:
         case 1:
              addTask()
         case 2:
              displayTask()
         case 3:
              print()
              for task in tasks:
                 print(f"TaskId: {task["id"]}, TaskName: {task["name"]}")
              id = int(input("Select id of task to edit: " ))
              updateTask(id)
         case 4:
              print()
              for task in tasks:
                 print(f"Task name: {task["name"]} , taskId: {task["id"]}")
              
              task_to_delete = int(input("Enter the id of task to delete: "))
              deleteTask(task_to_delete)
         case 5:
              print("Exiting Program...")
              break
         case _:
              print("Invalid Operation")



     