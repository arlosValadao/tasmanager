class Tarefa:
    def __init__(self, titulo: str, descricao: str, prioridade: int):
        self.__titulo: str = titulo
        self.__descricao: str = descricao
        self.__prioridade: int = prioridade

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def get_prioridade(self):
        return self.__prioridade

    def set_prioridade(self, prioridade: int) -> None:
        if 4 > prioridade > 0:
            self.__prioridade = prioridade
        else:
            return None
