from hashlib import sha512
from os import chdir, system, name, mkdir
from os import sep
from pickle import dump, load
from time import sleep
from User import *

'''
sep is the char that the operating system use for to differentiate directories of files
'''


# Has a string as a parameter
# Encrypt the string using SHA512 algorithm of encryption
# Returns a hash SHA512 of string (senha) in hexadecimal format
def encrypt(password: str) -> str:
    digest = sha512()
    digest.update(password.encode('utf-8'))
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
    print('_' * 33)
    print()
    print("|     GERENCIADOR DE TAREFAS    |")
    print('_' * 33)
    print()
    print("[ 1 ] - Cadastrar novo usuario")
    print('[ 2 ] - Logar no sistema')
    print("[ 3 ] - Sair do sistema")
    return read_int()


# Show the options available for the
# changes of tasks
# Returns read_int function
# i set the return as int because i can't
# uses a function as return indicator
# ex: (def main_menu() -> read_int)
def task_change_menu():
    cls()
    print("\033[1m[ 1 ] - Alterar titulo\033[m")
    print("\033[1m[ 2 ] - Alterar descricao\033[m")
    print("\033[1m[ 3 ] - Alterar prioridade\033[m")
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
    print()
    print("\033[1m[ 1 ] - Prioridade Alta\033[m")
    print("\033[1m[ 2 ] - Prioridade Media\033[m")
    print("\033[1m[ 3 ] - Prioridade Baixa\033[m")
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
def autenticate_user(login: str, password: str, file_name: str) -> bool:
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line = line[:-1].split(' ')
            # Verifying login and passwd
            if login == line[0] and line[1] == encrypt(password):
                return True
        # Case the login and passwd entered are not correct
        return False


# Has 3 string as parameter, name of directory that storage all the tasks of system,
# the path root of script and the name of user logged
# The function verifies and creates (if necessary) all files necessary
# for the correct functionament of system, post login
def verify_files_post_login(NAME_TASKS_DIR: str, SCRIPT_ROOT_PATH: str, login: str) -> None:
    # Verifying existence of directory that storage the tasks of sysem
    make_dir(NAME_TASKS_DIR)
    # Verifying existence of directory that storage the tasks of user registered
    # The directory has the name of user registered
    make_dir(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login)
    # Changing for the directory that have the name of user registered
    # and storage yours tasks and id of tasks
    chdir(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login)
    # Verifying existence of binary file that storage tasks and id of tasks of user registered
    if create_file(login + "_tasks.pbl", 1):
        write_b([], login + "_tasks.pbl")
    # File that storage the value of tasks id of user
    if create_file(login + "_info.pbl", 1):
        write_b(0, login + "_info.pbl")
    # Back to root path of script
    chdir(SCRIPT_ROOT_PATH)
    return None


# Has a string (file name), an integer (type of file)
# For the file type, 0 symbolizes a file in text mode
# and any number different of 0 symbolizes a file in binary mode
# Returns a int, 1 case the file was successful created
# and 0 otherwise
def create_file(file_name: str, file_type: int) -> int:
    try:
        # Conditional assignment
        file = open(file_name, 'x') if file_type == 0 else open(file_name, 'xb')
        file.close()
        return 1
    except FileExistsError:
        return 0


# Has as parameter a variable user of User data type
# and a string (name of file that the informations will registered)
# Register a user to a text file (writes the user's name and password to the file)
# that storage all users of system
# Returns None
def register_user(user: User, file_name: str) -> None:
    # Inserting the nickname and hash of user on file that storage
    # all users of system
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(user.get_name() + " " + encrypt(user.get_password()) + '\n')
    return None


# Has two strings as parameter, the first is a login and the 
# second is the name of file
# The function verify if the login typed already is
# inclued in the file
# Returns True case the file already exists and False otherwise
def login_exists(login: str, file_name: str) -> bool:
    with open(file_name, encoding="utf-8") as file:
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
def read_b(file_name: str) -> list:
    file_lines = []
    # Abrindo o arquivo para leitura
    file = open(file_name, "rb")
    while True:
        try:
            file_lines.append(load(file))
        # End Of File
        except EOFError:
            file.close()
            return file_lines


# Has a string as parameter
# Displays the message in bold and
# colored red on the screen
# Returns None
def alert(message: str) -> None:
    print("\033[1;31m{}\033[m".format(message))
    return None


# Has a string and a value as parameter
# Writes the value in file (file_name)
# Returns None
def write_b(value, file_name: str) -> None:
    file = open(file_name, "wb")
    dump(value, file)
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