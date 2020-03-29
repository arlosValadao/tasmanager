from Task import *
class User:
    def __init__(self, name: str, password: str):
        self.__name: str = name
        self.__password: str = password
        self.__tasks: list = []


    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
            self.__name = name
            return

    def get_password(self) -> str:
        return self.__password

    def get_tasks(self) -> list:
        return self.__tasks

    def set_tasks(self, tasks: list) -> None:
        self.__tasks = tasks
        return

    def add_task(self, task: Task) -> None:
        # Inserting tasks in decreasing priority mode from high to low priority
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
        return