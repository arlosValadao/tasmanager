class Task:
    def __init__(self, id: int, title: str, description: str, priority: int):
        self.__title: str = title
        self.__description: str = description
        self.__priority: int = priority
        self.__id = id


    def get_title(self):
        return self.__title

    def set_title(self, title: str):
        if type(description) == "<class 'str'>":
            self.__title = title
        return -1

    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_description(self):
        return self.__description

    def set_description(self, description: str):
        if type(description) == "<class 'str'>":
            self.__description = description
        return -1

    def get_priority(self):
        return self.__priority

    def set_priority(self, priority: int):
        if 4 > priority > 0:
            self.__priority = priority
        return -1