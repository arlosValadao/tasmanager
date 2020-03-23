from hashlib import sha512
from os import system, name, mkdir, sep, path
from pickle import dump, load
from time import sleep
from User import *
from prettytable import PrettyTable


'''
sep is the char that the operating system use for to differentiate directories of files
'''

# It has a string as a parameter
# Encrypt the string using SHA512 algorithm of encryption
# Returns a hash SHA512 of string (password) in hexadecimal format
def encrypt(password: str) -> str:
    digest = sha512()
    digest.update(password.encode('utf-8'))
    return digest.hexdigest()


# It doesn't have parameter
# Clear the screen
# Returns None
def cls() -> None:
    system('cls' if name == 'nt' else 'clear')
    return


# It doesn't have parameter
# The function "read an integer"
# It forces the user to enter an integer value
# Returns the value typed
def read_int() -> int:
    while True:
        try:
            integer = int(input('> '))
            return integer
        except ValueError:
            pass


# It doesn't have parameter
# Main menu of system
# Show the options for the user
# Returns the function read_int
# I set the return as int because I can't
# use a function as return indicator
# ex: (def main_menu() -> read_int)
def main_menu() -> int:
    print('_' * 33)
    print()
    print("|     TASK MANAGER           |")
    print('_' * 33)
    print()
    print("[ 1 ] - Register new user")
    print('[ 2 ] - Login the system')
    print("[ 3 ] - Exit of system")
    return read_int()


# It doesn't have parameter
# Shows the options available for
# changes of tasks
# Returns read_int function
# I set the return as int because I can't
# use a function as return indicator
# ex: (def main_menu() -> read_int)
def task_change_menu() -> int:
    print("\033[1m[ 1 ] - Change title\033[m")
    print("\033[1m[ 2 ] - Change description\033[m")
    print("\033[1m[ 3 ] - Change priority\033[m")
    return read_int()


# It doesn't have parameter
# Shows the options available for the user
# logged in the system
# Returns read_int function
# I set the return as int because I can't
# use a function as return indicator
# ex: (def main_menu() -> read_int)
def sub_menu() -> int:
    print('_' * 33)
    print()
    print("|       WELLCOME         |")
    print('_' * 33)
    print()
    print("[ 1 ] - Register new task")
    print("[ 2 ] - See tasks")
    print("[ 3 ] - Change task")
    print("[ 4 ] - Remove task")
    print("[ 5 ] - sign out account")
    return read_int()


# It doesn't have parameter
# Shows a mini menu of priority of task to be registered
# Returns read_int function
# i set the return as int because i can't
# use a function as return indicator
# ex: (def main_menu() -> read_int)
def menu_priority_task() -> int:
    print("\033[1m  TASK  PRIORITY\033[m")
    print()
    print("\033[1m[ 1 ] - High\033[m")
    print("\033[1m[ 2 ] - Medium\033[m")
    print("\033[1m[ 3 ] - Low\033[m")
    return read_int()


# It doesn't have parameter
# Freezes screen during 4.2 seconds
# Returns None
def freeze_screen() -> None:
    sleep(4.2)
    return


# It has 3 parameters, 3 strings, login (name of user)
# password (pass of user) and the file name to be readed
# Authenticates the user on the system, respectively
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


# It has a string (filename) as parameter
# The function verify file existence
# Returns True if exists and False otherwise
def file_exists(file_name: str) -> bool:
    if path.exists(file_name):
        return True
    return False


# It has 3 strings as parameter, name of directory that storage all the tasks of system,
# the path root of script and the name of user logged, respectively
# The function verifies and creates (if necessary) all files necessary
# for the correct functionament of system, post login
# Returns None
def verify_files_post_login(NAME_TASKS_DIR: str, SCRIPT_ROOT_PATH: str, login: str) -> None:
    # Verifying existence of directory that storage the tasks of system
    make_dir(NAME_TASKS_DIR)
    # Verifying existence of directory that storage the tasks of registered user
    # The directory has the name of registered user (is sub direcotory of "NAME_TASK_DIR")
    make_dir(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login)
    # Verifying existence of binary file that storage tasks of registered user
    if create_file(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_tasks.pbl", 1):
        write_b([], SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_tasks.pbl")
    # Verifying existence of binary file that task id value of user
    if create_file(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_info.pbl", 1):
        write_b(0, SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login +sep + login + "_info.pbl")
    return


# It has a string, file name, filename that will be created
# and  an integer (type of file), respectively
# For the file type, 0 symbolizes a file in text mode
# and any number different of 0 symbolizes a file in binary mode
# Returns an int, 1 case the file was successful created
# and 0 otherwise
def create_file(file_name: str, file_type: int) -> int:
    if not file_exists(file_name):
        # Conditional assignment
        file = open(file_name, 'x') if file_type == 0 else open(file_name, 'xb')
        file.close()
        return 1
    return 0


# It has as parameter a user  of User data type
# and a string (filename that the information will register), respectively
# Registers a user to a text file (writes the user's name and password to the file)
# that storage all users of system
# Returns None
def register_user(user: User, file_name: str) -> None:
    # Inserting the nickname and hash of user on file that storage
    # all users of system
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(user.get_name() + " " + encrypt(user.get_password()) + '\n')
    return


# It has 2 strings as parameter, the first is a login (username)and the
# second is the filename, file will to be verified login
# The function verify if the login typed already is
# inclued in the file
# Returns True case the file already exists and False otherwise
def login_exists(login: str, file_name: str) -> bool:
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            # Line converting in a list with login and password of user
            line = line.split(' ')
            if line[0] == login:
                return True
        return False


# It has a string as parameter, filename to  be read
# Read a binary file
# Returns "first line of file". Object
def read_b(file_name: str):
    with open(file_name, "rb") as file:
        return load(file)


# It has a string as parameter, message
# to be shown
# Displays the message in bold and
# colored red on the screen
# Returns None
def alert(message: str) -> None:
    print("\033[1;31m{}\033[m".format(message))
    return


# It has a string and a value (can be anything) as parameter
# Writes the value in file (file_name)
# Returns None
def write_b(value, file_name: str) -> None:
    file = open(file_name, "wb")
    dump(value, file)
    file.close()
    return


# It has as parameter a string, the directory or the directory + path
# The function make a directory
# Returns 1 when the file is created successful  and 0
# otherwise, when already exists the file or
# the name path is invalid
def make_dir(dir_name: str) -> int:
    if dir_name and not file_exists(dir_name):
        # Creating the directory
        mkdir(dir_name)
        return 1
    return 0


# It has an id (user task id)
# and a list (task list of user) as a parameter
# The function search the task with entered id
# Returns the task position on task list,
# otherwise returns -1
def find_task(task_list: list, id: int) -> int:
    # Binary search algorithm
    start = 0
    fim = len(task_list) - 1
    while start <= fim:
        mid = (start + fim) // 2
        if task_list[mid].get_id() == id:
            return mid
        elif id > task_list[mid].get_id():
            start = mid + 1
        else:
            fim = mid - 1
    return -1


# It has an id (int) and a list (user task list) as parameter
# The function remove the task with id entered
# of task list of user
# Returns True if remove operations was successful
# and False otherwise
def remove_task(task_list: list, id: int) -> bool:
    task_index_searched = find_task(task_list, id)
    if task_index_searched > -1:
        task_list.__delitem__(task_index_searched)
        return True
    return False


# It has a list (user task list) as parameter
# Convert Task objects to lists and adds all
# in a table (of PrettyTable module).
# Show the tasks of user in table format
# Returns True if operation was successful
# and False otherwise
def show_tasks(task_list: list) -> bool:
    if task_list:
        table = PrettyTable()
        table.field_names = ["ID", "TITLE", "DESCRIPTION", "PRIORITY"]
        # "Converting" the task to lists and adding the list in table (rows)
        for task in task_list:
            if task.get_priority() == 1:
                table.add_row([task.get_id(), task.get_title(), task.get_description(), "High"])
            elif task.get_priority() == 2:
                table.add_row([task.get_id(), task.get_title(), task.get_description(), "Medium"])
            else:
                table.add_row([task.get_id(), task.get_title(), task.get_description(), "Low"])
        print(table)
        return True
    return False


# It has a list (user task list), task_id, tile, description
# and priority as parameter,
# The function modify a task, it overwrites information
#  of task searched in task list
# Returns True if operation was successful
# and False otherwise
def modify_task(task_list: str, task_index: int, title: str, description: str, priority: int) -> None:
    modified_task = task_list[task_index]
    modified_task.set_title(title)
    modified_task.set_description(description)
    modified_task.set_priority(priority)
    alert("\tChanged  Task:")
    show_tasks([modified_task])
    return