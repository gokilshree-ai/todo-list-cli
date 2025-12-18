tasks = []

while True:
    task = input("Enter a task (or 'exit'): ")
    if task == "exit":
        break
    tasks.append(task)

print("Your To-Do List:")
for t in tasks:
    print("-", t)
