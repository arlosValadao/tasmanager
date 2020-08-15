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
        for i in range(len(self.__tasks)):
            if self.__tasks[i].get_priority() > task.get_priority():
                self.__tasks.insert(i, task)
                break
        else:
            self.__tasks.append(task)
        return