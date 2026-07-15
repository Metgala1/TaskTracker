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



     