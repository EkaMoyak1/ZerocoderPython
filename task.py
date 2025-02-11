class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def show(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        print(f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}")


def add_task(description, due_date):
    task = Task(description, due_date)
    tasks.append(task)
    print(f"Задача добавлена: {description}")

def complete_task(task):
   if not task.completed:
        task.completed = True
        print(f"Задача выполнена: {task.description}")
   else:
        print(f"Задача ранее выполнена: {task.description}")

def show_current_tasks():
    print("Текущие задачи:")
    for task in tasks:
        if not task.completed:
            task.show()

def show_all_tasks():
    print("Все задачи:")
    for task in tasks:
        task.show()



tasks = []

tasks.append(Task("Купить продукты", "2023-10-15"))
tasks.append(Task("Сделать домашнее задание", "2023-10-20"))
tasks.append(Task("Позвонить другу", "2023-10-25"))

show_all_tasks()

task = tasks[2]
complete_task(task)
show_current_tasks()
