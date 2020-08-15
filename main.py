from functions import *
from User import *
from Task import *
from os import getcwd, sep


SCRIPT_ROOT_PATH = getcwd()
NAME_USERS_FILE = "users.txt"
NAME_TASKS_DIR = "tasks"
exits: str = 'n'


while exits != "y":
    selected_option = 0
    while selected_option != 3:
        cls()
        selected_option = main_menu()
        if selected_option == 1:
            nick = input("\033[1mType your name: \033[m")
            if nick.strip().isidentifier():
                nick = nick.strip()
                create_file(NAME_USERS_FILE, 0)
                if login_exists(nick, NAME_USERS_FILE):
                    alert("The entered nick already exists int the system")
                    alert("Please, try again")
                    freeze_screen()
                else:
                    password = input("\033[1mType your password: \033[m")
                    alert("Registering user...")
                    new_user = User(nick, password)
                    register_user(new_user, NAME_USERS_FILE)
                    alert("User successfully registered!")
                    freeze_screen()
            else:
                alert("Invalid nickname")
                alert("Your nickname must contain only alphanumeric characters and underline")
                freeze_screen()
        elif selected_option == 2:
            login = input("\033[1mType your name: \033[m")
            password = input("\033[1mType your password: \033[m")
            alert("Logging into the system...")
            create_file(NAME_USERS_FILE, 0)
            if autenticate_user(login, password, NAME_USERS_FILE):
                alert("Login was successful!")
                freeze_screen()
                verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                USER_TASK_FILE_PATH = SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_tasks.pbl"
                USER_INFO_FILE_PATH = SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login + sep + login + "_info.pbl"
                resurrected_user = User(login, password)
                verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                user_task_list = read_b(USER_TASK_FILE_PATH)
                resurrected_user.set_tasks(user_task_list)
                cls()
                sub_menu_option_selected = sub_menu()
                while 5 != sub_menu_option_selected:
                    if sub_menu_option_selected == 1:
                        task_title = input("\033[1mTask title: \033[m")
                        task_description = input("\033[1mTask description: \033[m")
                        while True:
                            task_priority = menu_priority_task()
                            if 0 < task_priority < 4:
                                break
                        verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                        task_id = read_b(USER_INFO_FILE_PATH)
                        task_id += 1
                        new_task = Task(task_id, task_title, task_description, task_priority)
                        verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                        resurrected_user.add_task(new_task)
                        write_b(resurrected_user.get_tasks(), USER_TASK_FILE_PATH)
                        write_b(task_id, USER_INFO_FILE_PATH)
                        alert("Making task...")
                        alert("Task created successfully")
                        freeze_screen()
                    elif sub_menu_option_selected == 2:
                        verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                        user_task_list = read_b(USER_TASK_FILE_PATH)
                        cls()
                        if not show_tasks(user_task_list):
                            alert("You haven't yet registered a task!")
                        print()
                        alert("\t\t </ENTER> TO CONTINUE")
                        input()
                    elif sub_menu_option_selected == 3:
                        verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                        user_task_list = read_b(USER_TASK_FILE_PATH)
                        if show_tasks(user_task_list):
                            alert("Task id you want to change?")
                            searched_task = read_int()
                            task_index_searched = find_task(user_task_list, searched_task)
                            if task_index_searched > -1:
                                while True:
                                    item = task_change_menu()
                                    if 0 < item < 4:
                                        break
                                if item == 1:
                                    modify_item = input("Type > ")
                                    modify_task(user_task_list, task_index_searched, modify_item,
                                                user_task_list[task_index_searched].get_description(),
                                                user_task_list[task_index_searched].get_priority())
                                elif item == 2:
                                    modify_item = input("Type > ")
                                    modify_task(user_task_list, task_index_searched, user_task_list[task_index_searched]
                                                .get_title(), modify_item,
                                                user_task_list[task_index_searched].get_priority())
                                elif item == 3:
                                    while True:
                                        modify_item = menu_priority_task()
                                        if 0 < modify_item < 4:
                                            break
                                    modify_task(user_task_list, task_index_searched, user_task_list[task_index_searched]
                                                .get_title(), user_task_list[task_index_searched].get_description(),
                                                modify_item)
                                verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                                write_b(user_task_list, USER_TASK_FILE_PATH)
                                resurrected_user.set_tasks(user_task_list)
                                freeze_screen()
                            else:
                                alert("There is no task with this id!")
                                alert("Please, try again")
                                freeze_screen()
                        else:
                            alert("You haven't yet registered tasks!")
                            freeze_screen()
                    elif sub_menu_option_selected == 4:
                        verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                        user_task_list = read_b(USER_TASK_FILE_PATH)
                        if show_tasks(user_task_list):
                            alert("Task id you want to remove?")
                            remove_id = read_int()
                            if remove_task(user_task_list, remove_id):
                                verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH, login)
                                write_b(user_task_list, USER_TASK_FILE_PATH)
                                resurrected_user.set_tasks(user_task_list)
                                alert("Removing task...")
                                alert("Task removed!")
                                freeze_screen()
                            else:
                                alert("There is no task with this id!")
                                alert("Please, try again")
                                freeze_screen()
                        else:
                            alert("You haven't yet registered tasks!")
                            freeze_screen()
                    cls()
                    sub_menu_option_selected = sub_menu()
                alert("Logging out of account... \033[m")
                alert("Wait...")
                freeze_screen()
            else:
                alert("Login and/or password is incorrects!")
                freeze_screen()
    alert("Do you wnat to leave? (y / n)")
    exits = input("> ").strip().lower()
alert("Exiting the program...")
alert("Wait...")
freeze_screen()
