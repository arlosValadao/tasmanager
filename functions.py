from hashlib import sha512
from os import getcwd, chdir, system, name, mkdir
from os import path, sep, listdir
from pickle import dump, load
from time import sleep
from Tarefa import *
from Usuario import *
from User import *

'''
sep is the char that the operating system use for to differentiate directories of files
'''

# Dir name that will to store the tasks of all users
NAME_DIR_TASKS = "tarefas"
# Path of file (script) funcoes
PATH_SCRIPT = getcwd()


# Has a string as a parameter
# Encrypt the string using SHA512 algorithm of encryption
# Returns a hash SHA512 of string (senha) in hexadecimal format
def encrypt(passwd: str) -> str:
    digest = sha512()
    digest.update(passwd.encode('utf-8'))
    return digest.hexdigest()


# Clear the screen
# Returns None
def cls() -> None:
    system('cls' if name == 'nt' else 'clear')
    return None


# Dont has parameters
# The function read an integer
# a digitar um valor do tipo inteiro
# it forces the user to enter an integer value
# Returns the value typed
def read_int() -> int:
    while True:
        try:
            integer = int(input('> '))
            return integer
        except ValueError:
            pass


# Main menu of system
# Show the options for the user
# Returns the function read_int
# i set the return as int because i can't
# uses a function as return indicator
# ex: (def main_menu() -> read_int)
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


# Show the options available for the user
# logged in the system
# Returns read_int function
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


# Show a mini menu of priority of task to be registered
# Returns read_int function
# i set the return as int because i can't
# uses a function as return indicator
# ex: (def main_menu() -> read_int)
def menu_priority_task() -> int:
    print("\033[1m  PRIORIDADE DA TAREFA\033[m")
    print("[ 1 ] - Prioridade Baixa")
    print("[ 2 ] - Prioridade Media")
    print("[ 3 ] - Prioridade ALta")
    return read_int()


# Dont has parameter
# Freeze screen during 4.2 seconds
# Returns None
def freeze_screen() -> None:
    sleep(4.2)
    return None


# Has 3 parameters, 3 strings, password of user, name of user
# and the file name to be manipulated
# Authenticates the user on the system
# Returns True, case the user was authenticated and False, otherwise
def autenticate_user(login: str, passwd: str, file_name: str) -> bool:
    with open(file_name, encoding = "utf-8") as file:
        for line in file:
            linha = line[:-1].split(' ')
            # Verifying login and passwd
            if login == line[0] and line[1] == encrypt(passwd):
                return True
        # Case the login and passwd entered are not correct
        return False


                                             # A funcao vai ir ate onde foi solicitada e voltar para onde foi chamada, sem esse negocio de caminho do arquivo
# Has two parameters, 2 strings, the name of file and the path of file.
# Verifies if the file exists, trough of file name
# Returns True case the file exists and False otherwise
def file_exists(file_name: str, path: str) -> bool:
    # Directory that the function was called
    source_path = getcwd()
    chdir(path)
    # Verifying if the file exists
    if path.exists(file_name):
        chdir(source_path)
        return True
    chdir(source_path)
    return False


# Has a string (file name), an integer (type of file)
# For the file type, 0 symbolizes a file in text mode
# and any number different of 0 symbolizes a file in binary mode
# Returns a int, 1 case the file was successful created
# and 0 otherwise
def create_file(file_name: str, file_type: int) -> int:
    try:
        # Conditional assignment
        arquivo = open(nome_arq, 'x') if tipo_arq == 0 else open(nome_arq, 'xb')
        arquivo.close()
        return 1
    except FileExistsError:
        return 0



'''# Tem como parâmetro uma lista do tipo list
# Ordena a lista de acordo com a prioridade
# Retorna a lista ordenada
def ordenar_tarefa(lista: list):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
'''


# Tem como parâmetro um objeto do tipo Usuario e uma string  # Mover isso daqui para o main, deixar a funcao de cadastrar o usuario somente para salvar o login e senha no arquivo
# o nome do arquivo no qual as informações vão ser gravadas
# Cadastra um usuário no sistema, melhor dizendo, insere
# o nome e senha do usuário no arquivo em modo de texto que
# guarda todos os usuários do sistema
def register_user(user: User, file_name: str) -> bool:
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


# Has two strings as parameter, the first is a login and the 
# second is the name of file
# The function verify if the login typed already is
# inclued in the file
# Returns True case the file already exists and False
# otherwise
def login_exists(login: str, file_name: str) -> bool:
        with open(file_name, encoding = "utf-8") as file:
            for line in file:
                # Converting the line in a list with login and password of user
                line = line.split(' ')
                if line[0] == login:
                    return True
            return False


# Has a string as parameter, name file
# Read a binary file
# Returns a tuple containing all lines of the file,
# each line is an item of tuple
def read_b(file_name: str) -> tuple:
    file_lines = []
    # Abrindo o arquivo para leitura
    file = open (file_name, "rb", encoding = "utf-8")
    while True:
        try:
            file_lines.append(load(file))
        #End Of File
        except EOFError:
            file.close()
            return tuple(file_lines)


'''# Tem como parâmetro uma string, o caminho
# que o usuário deseja ir
# Muda para o diretório e logo após retorna para
# onde foi chamado
# Retorna 1 caso ocorra tudo corretamente e False caso contrário
def mudar_diretorio(caminho: str) -> bool:
    return True'''


# Has an string (name of file), and another variable as parameter 
# (value), value can be anything supported for python.
# Append a value in a file binary mode
# Returns None
def append_b(value, file_name: str) -> None:
    file = open(nome_arq, "ab", encoding = "utf-8")
    dump(valor, file)
    file.close()
    return None


# Has as parameter an string, the directory or the directory + path
# The function make a directory
# Returns 1 when the file is create successful  and 0
# otherwise, when already exists the file or
# the path is invalid
def make_dir(dir_name: str) -> int:
    if dir_name:
        try:
        	# Creating the directory
            mkdir(dir_name)
            return 1
        # Case the directory already exists
        except FileExistsError:
        	return 0
        # Case the path doesnt exists
        except FileNotFoundError:
        	return 0
    return 0


# Tem como parâmetro uma string (nome do usuário, e tarefa
# do tipo tarefa
# Cadastra uma nova tarefa no usuário passado como argumento
def register_task(task: Task, user_name: str) -> bool:
    caminho_padrao = getcwd()
    caminho_arq_binario = getcwd() + sep + NAME_DIR_TASKS + sep + nome_usuario + sep
    # Mudando para o diretório onde se encontra o arquivo do usuário
    chdir(caminho_arq_binario)
    append_b(1, nome_usuario + '_tarefas.pbl')
    # Voltando para o diretório onde o script está
    chdir(caminho_padrao)
    return True
