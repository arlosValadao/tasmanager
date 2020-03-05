class User:
    def __init__(self, name: str, password: str) :
        self.__name: str = name
        self.__password: str = password

    def get_name(self):
        return self.__nome

    def set_name(self, name: str):
        if "str" not in type(nome):
            return None
        self.__name = name

    def get_passwd(self):
        return self.__passowrd

    def set_passwd(self, passowrd: str):
        if "str" not in type(passowrd):
            return None
        self.__password = password
