class Stack:

    def __init__(self):
        self.__stack_list = []

    def __str__(self):
        return ', '.join(self.__stack_list)

    def add_member(self, member):
        self.__stack_list.append(member)

    def delete_member(self):
        if len(self.__stack_list) == 0:
            return None
        return self.__stack_list.pop(-1)


class TaskManager:

    def __init__(self):
        self.tasks = dict()

    def new_task(self, task, priority):
        if priority in self.tasks:
            self.tasks[priority].add_member(task)
        else:
            self.tasks[priority] = Stack()
            self.tasks[priority].add_member(task)

    def __str__(self):
        if len(self.tasks) != 0:
            return '\n'.join(
                [
                    '{priority}: {task}'.format(priority=priorities, task=self.tasks[priorities])
                    for priorities in sorted(self.tasks.keys())
                ]
            )





