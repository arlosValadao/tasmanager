class Task:
    def __init__(self, title: str, description: str, priority: int):
    	self.__title: str = title
        self.__description: str = description
        self.__priority: int = priority
        self.__tasks: list = []

    def get_title(self):
        return self.__title

    def set_title(self, title: str):
    	if type(description) == "<class 'str'>":
        	self.__title = title
        return -1

    def get_description(self):
        return self.__description

    def set_description(self, description: str):
    	if type(description) == "<class 'str'>":
        	self.__description = description
        return -1

    def get_priority(self):
        return self.__prioridade

    def set_priority(self, priority: int):
        if 4 > priority > 0:
            self.__priority = priority
        return None

    def get_tasks():
    	return self.__tasks

    def set_tasks(tasks: list):
    	self.__tasks = tasks

    def set_task(task: Task):
    	if type(task) == "<class 'Task.Task'>"
    		if task.get_description == 1:				# Incomplete
    			self.__tasks.insert(task, 0)
    	return -1