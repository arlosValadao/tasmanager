from hashlib import sha512
from os import getcwd, chdir, system, name, mkdir
from os import path, sep, listdir
from pickle import dump, load
from time import sleep
from Tarefa import *
from Usuario import *
'''
sep é o caractere usado pelo SO para diferenciar pastas de arquivos
sep is the char that the operating system use for to differentiate directories of files
'''
# Nome do diretório que irá armazenar as tarefas dos usuários
# Dir name that will to store the tasks of all users
NAME_DIR_TASKS = "tarefas"
# Caminho onde o script se encontra
# Path of file (script) funcoes
PATH_SCRIPT = getcwd()


# Tem como parâmetro uma string
# Has a string as a parameter
# Encrypt the string using SHA512 algorithm of encryption
# Aplica a função hashing sha512 a string e retorna o digest
# Retorna uma hash SHA512 da senha em forma hexadecimal
# Return a hash SHA512 of string (senha) in hexadecimal format
def encrypt(passwd: str) -> str:
    digest = sha512()
    digest.update(passwd.encode('utf-8'))
    return digest.hexdigest()


# Clear the screen
# Limpa a tela do computador (funciona em linux e windows)
# Retorna None
# Return None
def cls() -> None:
    system('cls' if name == 'nt' else 'clear')
    return None


'''# Identifica o SO que roda na máquina do usuário
# Retorna 1 se o sistema for windows
# e -1 caso contrário
def identificar_SO() -> int:
    tipo_SO = name
    return 1 if tipo_SO == 'nt' else -1'''


# Não há parâmetro
# Dont has parameters
# A função lê um inteiro, ou seja, ela obriga o usuário
# The function read an integer
# a digitar um valor do tipo inteiro
# it forces the user to enter an integer value
# Retorna o valor digitado
# Return the value typed
def read_int() -> int:
    while True:
        try:
            integer = int(input('> '))
            return integer
        except ValueError:
            pass


# Menu principal do sistema
# Main menu of system
# Exibe as opções para o usuário
# Show the options for the user
# Retorna a função ler_inteiro
# Return the function read_int
# Porém coloquei que retorna um inteiro pois a
# i set the return as int because i can't
# uses a function as return indicator
# ex: (def main_menu() -> read_int)
# a função leia_inteiro retorna um inteiro
def main_menu() -> int:
    cls()
    print('_' * 33)
    print()
    print("|     GERENCIADOR DE TAREFAS    |")
    print('_' * 33)
    print()
    print("[ 1 ] - Cadastrar novo usuario")
    print('[ 2 ] - Logar no sistema')
    print("[ 3 ] - Sair do sistema")
    return read_int()


# Exibe as opções disponíveis para
# os usuários logados no sistema
# Show the options available for the user
# logged in the system
# Retorna a função ler_inteiro
# Return read_int function
# i set the return as int because i can't
# uses a function as return indicator
# ex: (def main_menu() -> read_int)
def sub_menu() -> int:
    cls()
    print("[ 1 ] - Cadastrar nova Tarefa")
    print("[ 2 ] - Visualizar Tarefas")
    print("[ 3 ] - Alterar Tarefa")
    print("[ 4 ] - Excluir Tarefa")
    print("[ 5 ] - Sair")
    return read_int()


# Exibe o mini menu da prioridade da tarefa a cadastrada
# Show a mini menu of priority of task to be registered
# Retorna a função ler_inteiro
# Return read_int function
# Porém coloquei que retorna um inteiro pois a
# a função leia_inteiro retorna um inteiro
# i set the return as int because i can't
# uses a function as return indicator
# ex: (def main_menu() -> read_int)
def menu_priority_task() -> int:
    print("\033[1m  PRIORIDADE DA TAREFA\033[m")
    print("[ 1 ] - Prioridade Baixa")
    print("[ 2 ] - Prioridade Media")
    print("[ 3 ] - Prioridade ALta")
    return read_int()


# Não possui parâmetros
# Dont has parameter
# Congela a tela durante 4.2 segundos
# Freeze screen during 4.2 seconds
# Retrona None
# Return None
def freeze_screen() -> None:
    sleep(4.2)
    return None


# Tem como parâmetro, três strings, senha do usuário, nome do
# usuário e o nome do arquivo a ser manipulado
# Has 3 parameters, 3 strings, password of user, name of user
# and the file name to be manipulated
# Autentica o usuário no sistema
# Authenticates the user on the system
# Retorna True caso o usuário for autenticado com sucesso
# e False caso contrário
# Return True, case the user was authenticated and False, otherwise
def autenticate_user(login: str, passwd: str, file_name: str) -> bool:
    with open(file_name) as file:
        for line in file:
            linha = line[:-1].split(' ')
            # Verificando se o login e senha digitados estão corretos
            # Verify login and passwd
            if login == line[0] and line[1] == encrypt(passwd):
                return True
        # Caso o login e senha digitados não estejam corretos
        # Case the login and passwd entered are not correct
        return False


# Tem como parâmetro duas strings, o nome do arquivo a ser verificado
# e o caminho a ser verificado, por padrão ele tem como valor o caminho  # A funcao vai ir ate onde foi solicitada e voltar para onde foi chamada, sem esse negocio de caminho do arquivo
# atual do arquivo .py
# Verifica se um arquivo existe, pelo nome
# Retorna True caso o arquivo exista, e False caso não
def file_exists(file_name: str, path: str = getcwd()) -> bool:
    # Caminho onde o script se localiza
    global CAMINHO_SCRIPT
    # Mudando para o diretório do caminho informado pelo usuário
    chdir(caminho)
    # Verificando se o arquivo existe
    if path.exists(nome_arq):
        # Voltando para o diretório onde o script se localiza
        chdir(CAMINHO_SCRIPT)
        return True
    # Voltando para o diretório onde o script se localiza
    chdir(CAMINHO_SCRIPT)
    return False


# Tem como parâmetro uma string, o nome do arquivo
# e um inteiro, o tipo do arquivo, respectivamente.
# Para o tipo do arquivo: 0- simboliza arquivo
# em modo de texto e qualquer numero diferente
# de 0 simboliza o arquivo em modo binário
# Cria um arquivo de texto ou binário
# Retorna 1 caso o arquivo foi criado com sucesso
# Retorna 0 caso o arquivo já exista
def create_file(file_name: str, file_type: int) -> int:
    try:
        # Criando o arquivo
        arquivo = open(nome_arq, 'x') if tipo_arq == 0 else open(nome_arq, 'xb')
        arquivo.close()
        return 1
    except FileExistsError:
    	pass
    return 0



# Tem como parâmetro uma lista do tipo list
# Ordena a lista de acordo com a prioridade
# Retorna a lista ordenada
def ordenar_tarefa(lista: list):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]



# Tem como parâmetro um objeto do tipo Usuario e uma string  # Mover isso daqui para o main, deixar a funcao de cadastrar o usuario somente para salvar o login e senha no arquivo
# o nome do arquivo no qual as informações vão ser gravadas
# Cadastra um usuário no sistema, melhor dizendo, insere
# o nome e senha do usuário no arquivo em modo de texto que
# guarda todos os usuários do sistema
def cadastrar_usuario(usuario: Usuario, nome_arq: str) -> bool:
    # Gravando o nome e o hash da senha do usuário no arquivo "nome_arq"
    with open(nome_arq, 'a', encoding = 'utf-8') as arquivo:
        arquivo.write(usuario.get_nome() + " " + encrypt(usuario.get_senha()) + '\n')
    # Criando o diretório com o nome do usuário e que irá guardar suas tarefas
    criar_diretorio(usuario.get_nome(), PATH_SCRIPT + sep + NAME_DIR_TASKS)
    # Caminho onde o arquivo binário será criado
    caminho_arq_binario = PATH_SCRIPT + sep + NAME_DIR_TASKS + sep + usuario.get_nome() + sep
    # Mudando para o diretório onde será criado os arquivos binários
    chdir(caminho_arq_binario)
    # Criando o arquivo em modo binário que guarda as tarefas do usuário
    criar_arquivo(usuario.get_nome() + "_tarefas.pbl", 1)
    # Criando o arquivo em modo binário que guarda a ultima ocorrência do ID da tarefa
    criar_arquivo(usuario.get_nome() + ".i", 1)
    # Adicionando o valor do id no arquivo do usuario
    append_b(0, usuario.get_nome() + ".i")
    # Mudando para o caminho do script
    chdir(PATH_SCRIPT)
    # Mudando para o diretório onde se encontra o arquivo binário ".i"
    chdir(PATH_SCRIPT + sep + NAME_DIR_TASKS + sep + usuario.get_nome())
    # Voltando para o diretório do script
    chdir(PATH_SCRIPT)
    return True


# Tem como parâmetro duas strings a primeira refere-se ao login
# (nome do usuário) e o segundo corresponde ao nome do arquivo
# A função verifica se o login está contido no arquivo ou não
# Retorna True caso o nome já esteja contido e false caso não
def login_existe(login: str, nome_arq: str) -> bool:
    # Caso a string não seja vazia e os seus 4 últimos caracteres
    # seja igual a .txt
    if nome_arq[-4:] == ".txt":
        with open(nome_arq) as arquivo:
            for linha in arquivo:
                # Convertendo a linha em uma lista com dois elementos (login e senha do usuário)
                linha = linha.split(' ')
                # Verificando se o login digitado é igual à algum login existente no arquivo
                if linha[0] == login:
                    return True
            return False
    # Caso o nome do arquivo não contenha .txt como seus últimos 4 caracteres
    return False


# Tem como parâmetro uma string, o nome do arquivo a ser lido
# A função trabalha somente com arquivo .dat
# Lê um arquivo binário e retorna uma tupla contendo as linhas
# do arquivo, cada linha é um item da tupla.
def read_b(nome_arq: str) -> tuple:
    linhas = []
    # Abrindo o arquivo para leitura
    arquivo = open(nome_arq, 'rb', encoding = "utf-8")
    while True:
        try:
            # Adicionando a linha lida a lista de linhas
            linhas.append(load(arquivo))
        # Quando chegar ao fim do arquivo
        except EOFError:
            arquivo.close()
            return tuple(linhas)


'''# Tem como parâmetro uma string, o caminho
# que o usuário deseja ir
# Muda para o diretório e logo após retorna para
# onde foi chamado
# Retorna 1 caso ocorra tudo corretamente e False caso contrário
def mudar_diretorio(caminho: str) -> bool:
    return True'''


# Tem como parâmetro duas strings, nome_arq corresponde ao nome do arquivo
# a ser manipulado e texto corresponde a string a ser gravada no arquivo
# A função concatena texto no arquivo, ela abre o arquivo no modo append
# Retorna True caso consiga escrever no arquivo e False caso contrário
def append_b(valor, nome_arq: str) -> int:
    arquivo = open(nome_arq, "ab", encoding = "utf-8")
    dump(valor, arquivo)
    arquivo.close()
    return 1


'''IMPORTANTE
Nesse pequeno texto descrevo a maneira que encontrei de indentificar qual usuário está logado
no sistema, quando o usuário loga no sistema eu adiciono um caractere espaço no final da linha
que corresponde às informações dele'''


# Tem como parâmetro duas strings, a primeira corresponde ao nome da pasta
# e a segunda ao caminho, ou seja onde a pasta deve ser criada, por padrão, "caminho"
# é o caminho atual
# Retorna 1 caso consiga criar a pasta e 0 caso a pasta já exista ou o nome do diretório
# seja "null"
def criar_diretorio(nome_diretorio: str, caminho: str = getcwd()) -> int:
    # Caso o nome do diretório seja uma string nula
    if nome_diretorio:
        # Caminho onde o script se localiza
        global PATH_SCRIPT
        # Mudando de diretório informado pelo usuário
        chdir(caminho)
        try:
            # Criando o diretório
            mkdir(nome_diretorio)
            return 1
        except FileExistsError:
            pass
        finally:
            # Voltando para o diretório onde o script se localiza
            chdir(PATH_SCRIPT)
        return 0
    # Caso o nome do diretório seja uma string nula
    return 0


# Tem como parâmetro uma string (nome do usuário, e tarefa
# do tipo tarefa
# Cadastra uma nova tarefa no usuário passado como argumento
def cadastrar_tarefa(tarefa: Tarefa, nome_usuario: str) -> bool:
    global PATH_SCRIPT
    caminho_padrao = getcwd()
    caminho_arq_binario = getcwd() + sep + NAME_DIR_TASKS + sep + nome_usuario + sep
    # Mudando para o diretório onde se encontra o arquivo do usuário
    chdir(caminho_arq_binario)
    append_b(1, nome_usuario + '_tarefas.pbl')
    # Voltando para o diretório onde o script está
    chdir(caminho_padrao)
    return True
