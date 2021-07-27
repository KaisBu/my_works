from stack import TaskManager


new_task_manager = TaskManager()

new_task_manager.new_task("to clean the room", 4)
new_task_manager.new_task("to wash the dishes", 4)
new_task_manager.new_task("to rest", 1)
new_task_manager.new_task("to eat", 2)

print(new_task_manager)

