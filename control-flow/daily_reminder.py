task = input("Enter your task: ")
priority = (input("Priority (high/medium/low): ")).lower()
time_bound = (input("Is it time-bound? (yes/no): ")).lower()

match priority:
  case "high": 
    if time_bound == "yes":
      print(task, "is a high priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(task, "is a high priority task that requires immediate attention today!")
    else : print("Task's time-bound property not identified")

  case "medium": 
    if time_bound == "yes":
      print(task, "is a medium priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(task, "is a medium priority task that requires immediate attention today!")
    else : print("Task's time-bound property not identified")
  
  case "low": 
    if time_bound == "yes":
      print(task, "is a low priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(task, "is a low priority task that requires immediate attention today!")
    else : print("Task's time-bound property not identified")

  case _: print("Task priority not identified")