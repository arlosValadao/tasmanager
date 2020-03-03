class Usuario:
    def __init__(self, nome : str, senha : str) :
        self.__nome : str = nome
        self.__senha : str = senha

    def get_nome(self) :
        return self.__nome

    def set_nome(self, nome : str):
        self.__nome = nome

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha : str):
        self.__senha = senha
