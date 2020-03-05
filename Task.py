class Task:
    def __init__(self, title: str, description: str, priority: int):
        self.__description: str = description
        self.__priority: int = priority

    def get_title(self):
        return self.__title

    def set_title(self, title: str):
    	if "str" not in type(title):
    		return None
        self.__title = title

    def get_description(self):
   		if "str" not in title:
    		return None
        return self.__description

    def set_description(self, description: str):
    	if "str" not in type(description):
    		return None
        self.__description = description

    def get_priority(self):
        return self.__prioridade

    def set_priority(self, priority: int):
        if 4 > priority > 0:
            self.__priority = priority
        return None