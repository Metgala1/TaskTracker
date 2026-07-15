import datetime
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



     