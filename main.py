from funcoes import *
from Usuario import Usuario              # Colocar para que o nick seja composto somnete de caraacteres alfanuméricos e o underline
from Tarefa import Tarefa
from getpass import getpass
'''
getpass faz a animação de não ecoar na tela os caracteres que são digitados pelo usuário, ela é implementada
no momento que o usuário vai fazer o login, por isso, não pense que o seu teclado tá com problema :)
'''

# Nome do arquivo que guarda os usuários cadastrados no sistema
# Name of file that store the users registered in the system
NOME_ARQUIVO = "users.txt"
# Nome do diretório que irá armazenar as tarefas dos usuários
# Name of directory that will storage the tasks of users
NOME_DIRETORIO_TAREFAS = "tarefas"
######################################################
#                                                    #
#           CRIANDO OS ARQUIVOS NECESSÁRIOS          #
#                                                    #
######################################################

# Criando o diretório que irá armazenar as tarefas dos usuários
# Creating the directories that will store the tasks of all users
criar_diretorio(NOME_DIRETORIO_TAREFAS)
# Criando o arquivo que irá armazenar os usuários cadastrados no sistema
# Creating the file that storage the hashs and nickname of all users of system
criar_arquivo(NOME_ARQUIVO, 0)
# FALTA CRIAR O ARQUIVO BINÁRIO, MAS RELAXE


selected_option = 0
while selected_option != 3:
    opcao_menu = main_menu()
    # Caso o usuário escolha cadastrar uma novo usuário
    # Case the user wants register a new user in the system
    if selected_option == 1:
        while True:
            nick = input("\033[1mEntre com o seu nick: \033[m")
            # Verificando se o nome digitado é valido
            # Validating the nickname typed
            if nick.strip().isidentifier():
                nick = nick.strip()
                # Verificando se o login digitado existe no arquivo informado
                if login_existe(nick, NOME_ARQUIVO):
                    print("\033[1;31mO nick informado já está cadastrado no sistema \033[1m")
                    print("\033[1;31mPor favor, tente outro nick \033[m")
                    freeze_screen()
                else:
                    passwd = input("\033[1mEntre com a sua senha: \033[m")
                    break
            # Caso o nick não seja válido
            else:
                print("\033[1;31mNick inválido \033[m")
                print("\033[1;31mO seu nick deve ser composto somente por caracteres alfanumericos e underline \033[m")
                freeze_screen()
        print("\033[1;31mCadastrando...\033[m")
        print("\033[1;31mUsuario cadastrado com sucesso!\033[m")
        # Instanciando o objeto do tipo usuário
        new_user = Usuario(nick, passwd)
        # Cadastrando o usuário no sistema
        cadastrar_usuario(new_user, NOME_ARQUIVO)
        freeze_screen()

    # Caso o usuário escolha logar no sistema
    # Case the user want log in the system
    elif selected_option == 2:
        while True:
            login = input("\033[1mDigite o seu login: \033[m")
            passwd = getpass("\033[1mDigite a sua senha: \033[m")
            print("\033[1;31mLogando no sistema... \033[m")
            # Autenticando o usuário no sistema
            # Authenticating the user in the system
            if autenticate_user(login, passwd, NOME_ARQUIVO):
                print("\033[1;31mLogin realizado com sucesso! \033[m")
                freeze_screen()
                selected_option_sub = sub_menu()
                while 5 != selected_option_sub:
                    # Caso o usuário escolha criar uma nova tarefa
                    # Case the user want create a new task
                    if selected_option_sub == 1:
                        # Pedindo as informações da tarefa
                        # requesting informations about task
                        task_titule = input("\033[1mTitulo da tarefa: \033[m")
                        task_description = input("\033[1mDescricao da tarefa: \033[m")
                        task_priority = menu_priority_task()
                        # Instanciando o objeto da classe Tarefa
                        new_tarefa = Tarefa(task_titule, task_description, task_priority)
                # Caso o usuário saia da conta
                # Case the user logout of account
                print("\033[1mDeslogando da conta... \033[m")
                print('\033[1mAguarde... \033[m')
                freeze_screen()
                break
            # Caso o login e/ou senha incorretos
            # Case login and/or password entered are incorrect
            else:
                print("\033[1;31mLogin e/ou senha incorretos! \033[m")
print("\033[1mSaindo do programa... \033[1m")
freeze_screen()
