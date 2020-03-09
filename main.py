from functions import *
from User import *
from Task import *
from getpass import getpass
from os import getcwd
'''
getpass faz a animação de não ecoar na tela os caracteres que são digitados pelo usuário, ela é implementada
no momento que o usuário vai fazer o login, por isso, não pense que o seu teclado tá com problema :)
'''

# Source path of script main obviously this can change with each script execution
SCRIPT_ROOT_PATH = getcwd()
# Name of file that store the users registered in the system
NAME_USERS_FILE = "users.txt"
# Name of directory that will storage the tasks of users
NAME_TASKS_DIR = "tasks"
######################################################
#                                                    #
#           CRIANDO OS ARQUIVOS NECESSÁRIOS          #
#                                                    #
######################################################

# Creating the directories that will store the tasks of all users
make_dir(NAME_TASKS)
# Creating the file that storage the hashs and nickname of all users of system
create_file(NAME_USERS_FILE, 0)


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
                # Verifying existence of directory that storage the tasks of sysem
                make_dir(NAME_TASKS_DIR)
                # Verifying existence of directory that storage the tasks of user registered
                # The directory has the name of user registered
                make_dir(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + sep + login)
                # Changing for the directory that have the name of user registered
                # and storage yours tasks and id of tasks
                chdir(SCRIPT_ROOT_PATH + sep + NAME_TASKS_DIR + login)
                # Verifying existence of binary file that storage tasks and id of tasks of user registered
                create_file(NAME_USERS_FILE, 1)
                create_file(NAME_USERS_FILE, 1)
                # Back to root path of script
                chdir(SCRIPT_ROOT_PATH)
                freeze_screen()
                selected_option_sub = sub_menu()
                while 5 != selected_option_sub:
                    # Case the user want create a new task
                    if selected_option_sub == 1:
                        # requesting informations about task
                        task_titule = input("\033[1mTitulo da tarefa: \033[m")
                        task_description = input("\033[1mDescricao da tarefa: \033[m")
                        task_priority = menu_priority_task()
                        # Making a task object
                        new_tarefa = Tarefa(task_titule, task_description, task_priority)
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

