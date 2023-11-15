class TodoList:
    def __init__(self):
        self.tasks = []
        pass

    def add(self, todo):
        self.tasks.append(todo)
      
    def incomplete(self):
        incomplete = []
        for task in self.tasks:
            if task.complete == False:
                incomplete.append(task.task)
        return incomplete

    def complete(self):
        complete = []
        for task in self.tasks:
            if task.complete == True:
                complete.append(task.task)
        return complete
        

    def give_up(self):
        for task in self.tasks:
            task.mark_complete()