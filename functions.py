from hashlib import sha512
from os import system, name, mkdir, sep, path
from pickle import dump, load
from time import sleep
from User import *
from prettytable import PrettyTable


FREEZE_TIME = 2.7


def encrypt(password: str) -> str:
    digest = sha512()
    digest.update(password.encode('utf-8'))
    return digest.hexdigest()


def cls() -> None:
    system('cls' if name == 'nt' else 'clear')
    return


def read_int() -> int:
    while True:
        try:
            integer = int(input('> '))
            return integer
        except ValueError:
            pass


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


def task_change_menu() -> int:
    print("\033[1m[ 1 ] - Change title\033[m")
    print("\033[1m[ 2 ] - Change description\033[m")
    print("\033[1m[ 3 ] - Change priority\033[m")
    return read_int()


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


def menu_priority_task() -> int:
    print("\033[1m  TASK  PRIORITY\033[m")
    print()
    print("\033[1m[ 1 ] - High\033[m")
    print("\033[1m[ 2 ] - Medium\033[m")
    print("\033[1m[ 3 ] - Low\033[m")
    return read_int()


def freeze_screen() -> None:
    sleep(FREEZE_TIME)
    return


def autenticate_user(login: str, password: str, file_name: str) -> bool:
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line = line[:-1].split(' ')
            if login == line[0] and line[1] == encrypt(password):
                return True
        return False


def file_exists(file_name: str) -> bool:
    if path.exists(file_name):
        return True
    return False


def verify_files_post_login(NAME_TASKS_DIR: str, SCRIPT_ROOT_PATH: str, login: str) -> None:
    make_dir(NAME_TASKS_DIR)
    make_dir(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login)
    if create_file(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_tasks.pbl", 1):
        write_b([], SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_tasks.pbl")
    if create_file(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_info.pbl", 1):
        write_b(0, SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_info.pbl")
    return


def create_file(file_name: str, file_type: int) -> int:
    if not file_exists(file_name):
        file = open(file_name, 'x') if file_type == 0 else open(file_name, 'xb')
        file.close()
        return 1
    return 0


def register_user(user: User, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(user.get_name() + " " + encrypt(user.get_password()) + '\n')
    return


def login_exists(login: str, file_name: str) -> bool:
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line = line.split(' ')
            if line[0] == login:
                return True
        return False


def read_b(file_name: str):
    with open(file_name, "rb") as file:
        return load(file)


def alert(message: str) -> None:
    print("\033[1;31m{}\033[m".format(message))
    return


def write_b(value, file_name: str) -> None:
    file = open(file_name, "wb")
    dump(value, file)
    file.close()
    return


def make_dir(dir_name: str) -> int:
    if dir_name and not file_exists(dir_name):
        mkdir(dir_name)
        return 1
    return 0


def find_task(task_list: list, task_id: int) -> int:
    for i in range(len(task_list)):
        if task_list[i].get_id() == task_id:
            return i
    return -1


def remove_task(task_list: list, task_id: int) -> bool:
    task_index_searched = find_task(task_list, task_id)
    if task_index_searched > -1:
        task_list.__delitem__(task_index_searched)
        return True
    return False


def show_tasks(task_list: list) -> bool:
    if task_list:
        table = PrettyTable()
        table.field_names = ["ID", "TITLE", "DESCRIPTION", "PRIORITY"]
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


def modify_task(task_list: list, task_index: int, title: str, description: str, priority: int) -> None:
    modified_task = task_list.pop(task_index)
    modified_task.set_title(title)
    modified_task.set_description(description)
    modified_task.set_priority(priority)
    i = 0
    task_list_len = len(task_list)
    while i < task_list_len:
        if task_list[i].get_priority() > modified_task.get_priority():
            break
        i += 1
    task_list.insert(i, modified_task)
    alert("\tChanged  Task:")
    show_tasks([modified_task])
    return