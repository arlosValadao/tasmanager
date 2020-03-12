from Task import *
from prettytable import PrettyTable
class User:
    def __init__(self, name: str, password: str):
        self.__name: str = name
        self.__password: str = password
        self.__tasks: list = []


    def get_name(self) -> str:
        return self.__name


    def get_password(self) -> str:
        return self.__password


    def set_name(self, name: str) -> None:
            self.__name = name
            return


    def get_tasks(self) -> list:
        return self.__tasks


    def set_tasks(self, tasks: list) -> None:
        self.__tasks = tasks
        return


    def set_task(self, task: Task) -> None:
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


    # Has as parameter an id (user task id)
    # The function search the task with entered id
    # Returns the task position on task list,
    # otherwise returns -1
    def find_task(self, id: int) -> int:
        # Binary search algorithm
        start = 0
        fim = len(self.__tasks) - 1
        while start <= fim:
            mid = (start + fim) // 2
            if self.__tasks[mid].get_id() == id:
                return mid
            elif id > self.__tasks[mid].get_id():
                start = mid + 1
            else:
                fim = mid - 1
        return -1


    # Has an id (int) as parameter
    # The function remove the task with id entered
    # of task list of user
    # Returns True if remove operations was successful
    # and False otherwise
    def remove_task(self, id: int) -> bool:
        task_searched = self.find_task(id)
        if task_searched > -1:
            self.__tasks.__delitem__(task_searched)
            return True
        return False


    # Dont have parameters
    # Convert Task objects to lists and adds all
    # in a table (of PrettyTable module).
    # Show the tasks of user in table format
    def show_tasks(self) -> None:
        table = PrettyTable()
        table.field_names = ["ID", "TITULO", "DESCRICAO", "PRIORIDADE"]
        # Converting the task to lists and adding the list in table (rows)
        for task in self.__tasks:
            task_converted_2_list = []
            task_converted_2_list.append(task.get_id())
            task_converted_2_list.append(task.get_title())
            task_converted_2_list.append(task.get_description())
            #task_converted_2_list.append(task.get_priority())
            if task.get_priority() == 1:
                task_converted_2_list.append("Alta")
            elif task.get_priority() == 2:
                task_converted_2_list.append("Media")
            elif task.get_priority() == 3:
                task_converted_2_list.append("Baixa")
            table.add_row(task_converted_2_list)
        print(table)
        return None

