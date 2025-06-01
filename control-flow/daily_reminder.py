task = input("Describe the task")
priority = input("Describe priority level :high, medium or low")
time_bound = input("is the task time bound : yes or no")
match priority:
    case "high":
        if time_bound == "yes":
            print (f"finish this now! it requires immediate action!")
        else:
            print(f"try to finish this task, it is of high priority but you have time ")
    case "medium":
        if time_bound == "yes":
            print(f"this task is is of medium priority, but requires immediate ")
        else:
            print(f"this task is is of medium priority, but you can take our time ")
    case "low":
        if time_bound == "yes":
            print("this task is not very important but needs your attention")
        else:
            print("you can take your time to do this task ")
            
