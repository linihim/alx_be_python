task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ").lower()
time_bound = input("Is it time-bound?(Yes/No): ").lower()

match priority:
	case "high":
		message = f"'{task}' is a high priority task"
	case "medium":
		message = f"'{task}' is a medium priority task"
	case "low":
		message = f"'{task}' is a low priority task"
	case _:
		message = f"'{task}' has no priotity level"

if time_bound == "yes":
	full_message = message + "that requires immediate attention!"
	print("Reminder:", full_message)
else:
	if priority == "high":
		full_message = message + ". Make sure to complete it soon!"
		print("Note:", full_message)
	elif priority == "medium":
		full_message = message + ". Try to complete it soon if possible!"
		print("Note:", full_message)
	else:
		full_message = message + ". Complete it when you have time!"
		print("Note:", full_message)
