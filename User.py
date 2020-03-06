class User:
    def __init__(self, name: str, password: str) :
        self.__name: str = name
        self.__password: str = password
        self.__tasks: list = []

    def get_name(self):
        return self.__nome

    def set_name(self, name: str):
        if if type(description) == "<class 'str'>"::
            self.__name = name
        return -1
    def get_passwd(self):
        return self.__passowrd

    def set_passwd(self, passowrd: str):
        if type(description) == "<class 'str'>"::
            self.__password = password
        return -1
        
    def get_tasks():
        return self.__tasks

    def set_tasks(tasks: list):
        self.__tasks = tasks

    def set_task(task: Task):
        if type(task) == "<class 'Task.Task'>"
            if task.get_description == 1:               # Incomplete
                self.__tasks.insert(task, 0)
        return -1