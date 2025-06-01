# daily_reminder.py

# Prompt user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# React based on priority using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule time for it.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires attention today.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority level entered.")
