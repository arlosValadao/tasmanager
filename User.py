class User:
    def __init__(self, name: str, password: str) :
        self.__name: str = name
        self.__password: str = password

    def get_name(self):
        return self.__nome

    def set_name(self, name: str):
        self.__name = name

    def get_passwd(self):
        return self.__passowrd

    def set_passwd(self, passowrd: str):
        self.__password = password
