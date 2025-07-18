task = input("Give the description of your task?: ")
priority = (input("What is the task's priority? (high, medium, low): ")).lower()
time_bound = (input("is the task time-bound? (yes or no): ")).lower()

match time_bound:
  case "yes": print(task, "is a", priority, "priority task that requires immediate attention today!")
  case "no": print(task, "is a", priority, "priority task. Consider completing it when you have free time.")
  case _: print("Task priority not identified")