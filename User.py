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
        if "class" in str(type(task)):
            self.__tasks.append(task)
            return 0
        return -1

    # Orders the tasks through of priority. 1 to (until) 3
    # high priority to low priority
    def sort_tasks(self):
        print(self.__tasks[0])
        for i in range(len(self.__tasks) - 1):
            for j in range(i + 1, len(self.__tasks)):
                if self.__tasks[i].get_priority() > self.__tasks[j].get_priority():
                    self.__tasks[i], self.__tasks[j] = self.__tasks[j], self.__tasks[i]
        return None


'''usuario = User("stick-cup", "SENHA")
tarefa1 = Task('prova1', 'ga', 1)
tarefa2 = Task('prova2', 'ga', 2)
tarefa3 = Task('prova3', 'ga', 2)
tarefa4 = Task('prova4', 'ga', 2)
tarefa5 = Task('prova5', 'ga', 3)
tarefa6 = Task('prova6', 'ga', 1)

print(type(usuario))
print(usuario.get_name())
print(usuario.get_passwd())
# ADICIONANDO AS TAREFAS NA COLEÇÃO DO USUARIO
usuario.set_task(tarefa1)
usuario.set_task(tarefa2)
usuario.set_task(tarefa3)
usuario.set_task(tarefa4)
usuario.set_task(tarefa5)
usuario.set_task(tarefa6)
print("\t\t\tTAREFAS DO USUARIO")
print(usuario.get_tasks())
usuario.sort_tasks()
for teste in usuario.get_tasks():
    print(teste.get_priority())
    print(teste.get_title())'''