task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = f"'{task}' is a {priority} task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            print(reminder)
    case "low":
        reminder = f"Note: '{task}' is a low priority task.Consider completing it when you have free time!"
        print(reminder)
