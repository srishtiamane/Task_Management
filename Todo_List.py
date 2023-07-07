class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description} (Priority: {self.priority})"

class Todo_List:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_as_completed()
            print(f"Task '{task.description}' marked as completed.")
        else:
            print("Invalid task index.")

    def clear_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        for task in completed_tasks:
            self.tasks.remove(task)
        print("Completed tasks cleared.")

    def __str__(self):
        return f"TodoList: {len(self.tasks)} tasks"

todo_list = Todo_List()

task1 = Task("Buy groceries", "High")
task2 = Task("Finish homework", "Medium")
task3 = Task("Walk the dog", "Low")
todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

print(todo_list)
todo_list.display_tasks()

todo_list.mark_task_as_completed(2)
todo_list.display_tasks()

todo_list.clear_completed_tasks()
todo_list.display_tasks()
