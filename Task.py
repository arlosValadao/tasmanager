class Task:
    def __init__(self, titule: str, description: str, priority: int): # Change the priority for str type
        self.__titule: str = titule
        self.__description: str = description
        self.__priority: int = priority

    def get_titule(self):
        return self.__titule

    def set_titule(self, titule: str):
        self.__titulo = titule

    def get_description(self):
        return self.__description

    def set_descricao(self, description: str):
        self.__description = description

    def get_priority(self):
        return self.__prioridade

    def set_priority(self, priority: int):
        if 4 > priority > 0:
            self.__priority = priority
        return None
