class ToDo_list:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        self.name = name
        self.tasks = []
        pass 

    def add(self, task):
        if len(task) == 0:
            return None
        self.tasks.append(task)

    def show(self):
        if len(self.tasks) == 0:
            return f'You have nothing left todo {self.name}!'
        return_string = " " + self.tasks[0]
        if len(self.tasks) > 1:
            for each in self.tasks[1:len(self.tasks)]:
                return_string += ", " + each
        return f"Toms ToDo list:{return_string}"

    def complete(self, task):
        self.tasks.remove(task)