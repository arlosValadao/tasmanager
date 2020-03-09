from Task import *
class User:
    def __init__(self, name: str, password: str):
        self.__name: str = name
        self.__password: str = password
        self.__tasks: list = []

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if type(name) == "<class 'str'>":
            self.__name = name
        return -1

    def get_passwd(self):
        return self.__password

    def set_passwd(self, passowrd: str):
        if type(description) == "<class 'str'>":
            self.__password = password
        return -1
        
    def get_tasks(self):
        return self.__tasks

    def set_tasks(self, tasks: list):
        self.__tasks = tasks

    def set_task(self, task: Task):
        #Inserting tasks in decreasing priority mode from high to low priority
        # (taking into account that tasks can have high, medium or low priority)
        # and in increasing order of their ids
        # For example: High priority task in ascending order of ids. This is
        # analogous to the other priorities
        for i in range(len(self.__tasks)):
            if self.__tasks[i].get_priority() > task.get_priority():
                self.__tasks.insert(i, task)
                break
        else:
            self.__tasks.append(task)





