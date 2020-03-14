class Task:
    def __init__(self, id: int, title: str, description: str, priority: int):
        self.__title: str = title
        self.__description: str = description
        self.__priority: int = priority
        self.__id : int = id


    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title
        return

    def get_id(self) -> int:
        return self.__id

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description
        return

    def get_priority(self) -> int:
        return self.__priority

    def set_priority(self, priority: int) -> None:
        self.__priority = priority
        return