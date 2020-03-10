from functions import *
from User import *
from Task import *
from getpass import getpass
from os import getcwd, sep
'''
getpass faz a animação de não ecoar na tela os caracteres que são digitados pelo usuário, ela é implementada
no momento que o usuário vai fazer o login, por isso, não pense que o seu teclado tá com problema :)
'''

# Root path of script main obviously this can change with each script execution
SCRIPT_ROOT_PATH = getcwd()
# Name of file that store the users registered in the system
NAME_USERS_FILE = "users.txt"
# Name of directory that will storage the tasks of users
NAME_TASKS_DIR = "tasks"


selected_option = 0
while selected_option != 3:
    selected_option = main_menu()
    # Case the user wants register a new user in the system
    if selected_option == 1:
        while True:
            nick = input("\033[1mEntre com o seu nick: \033[m")
            # Validating the nickname typed
            if nick.strip().isidentifier():
                nick = nick.strip()
                # Verifying existence of file that storage users of system
                create_file(NAME_USERS_FILE, 0)
                # Verifying existence of typed nickname on system
                if login_exists(nick, NAME_USERS_FILE):
                    print("\033[1;31mO nick informado já está cadastrado no sistema \033[1m")
                    print("\033[1;31mPor favor, tente outro nick \033[m")
                    freeze_screen()
                else:
                    password = input("\033[1mEntre com a sua senha: \033[m")
                    break
            # Case invalid nickname
            else:
                print("\033[1;31mNick inválido \033[m")
                print("\033[1;31mO seu nick deve ser composto somente por caracteres alfanumericos e underline \033[m")
                freeze_screen()
        # User informations collected with successful
        print("\033[1;31mCadastrando...\033[m")
        # Making an object User
        new_user = User(nick, password)
        # Registering the user on system
        register_user(new_user, NAME_USERS_FILE)
        print("\033[1;31mUsuario cadastrado com sucesso!\033[m")
        freeze_screen()

    # Case the user want log in the system
    elif selected_option == 2:
        while True:
            login = input("\033[1mDigite o seu login: \033[m")
            password = getpass("\033[1mDigite a sua senha: \033[m")
            print("\033[1;31mLogando no sistema... \033[m")
            # Verifying existence of file that storage users of system
            create_file(NAME_USERS_FILE, 0)
            # Authenticating the user in the system
            if autenticate_user(login, password, NAME_USERS_FILE):
                print("\033[1;31mLogin realizado com sucesso! \033[m")
                verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH)
                # Object of user logged in system, at some point he was dead in file users.txt
                resurrected_user = User(login, password)
                sub_menu_option_selected = sub_menu()
                while 5 != sub_menu_option_selected:
                    # Case the user want create a new task
                    if sub_menu_option_selected == 1:
                        task_titule = input("\033[1mTitulo da tarefa: \033[m")
                        task_description = input("\033[1mDescricao da tarefa: \033[m")
                        task_priority = menu_priority_task()
                        # Making a task object
                        new_task = Task(task_titule, task_description, task_priority)
                        verify_files_post_login(NAME_TASKS_DIR, SCRIPT_ROOT_PATH)
                        # Path of file contains information about user
                        user_path = getcwd() + sep + NAME_TASKS_DIR + sep + login + sep
                        task_id = read_b(path_user + login + "_info.pbl")
                        task_id = task_id[0]
                        new_task.set_id(task_id)
                        resurrected_user.set_task(new_task)
                        write_b(resurrected_user.get_tasks(), user_path + login + "_tasks.pbl")
                        write_b()
                # Case the user logout of account
                print("\033[1mDeslogando da conta... \033[m")
                print('\033[1mAguarde... \033[m')
                freeze_screen()
                break
            # Case login and/or password entered are incorrect
            else:
                print("\033[1;31mLogin e/ou senha incorretos! \033[m")
# Exiting of system
print("\033[1mSaindo do programa... \033[1m")
freeze_screen()

