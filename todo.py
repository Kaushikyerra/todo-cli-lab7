tasks = []
def add_task(t): tasks.append(t)
def list_tasks(): print(tasks)
def add_task_cli():
    t=input('Task: ')
    add_task(t)
def delete_task(i): del tasks[i]
