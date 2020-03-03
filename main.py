from funcoes import *
from Usuario import Usuario              # Colocar para que o nick seja composto somnete de caraacteres alfanuméricos e o underline
from Tarefa import Tarefa
from getpass import getpass
'''
getpass faz a animação de não ecoar na tela os caracteres que são digitados pelo usuário, ela é implementada
no momento que o usuário vai fazer o login, por isso, não pense que o seu teclado tá com problema :)
'''

# Nome do arquivo que guarda os usuários cadastrados no sistema
NOME_ARQUIVO = "users.txt"
# Nome do diretório que irá armazenar as tarefas dos usuários
NOME_DIRETORIO_TAREFAS = "tarefas"
######################################################
#                                                    #
#           CRIANDO OS ARQUIVOS NECESSÁRIOS          #
#                                                    #
######################################################

# Criando o diretório que irá armazenar as tarefas dos usuários
criar_diretorio(NOME_DIRETORIO_TAREFAS)
# Criando o arquivo que irá armazenar os usuários cadastrados no sistema
criar_arquivo(NOME_ARQUIVO, 0)
# FALTA CRIAR O ARQUIVO BINÁRIO, MAS RELAXE


opcao_menu = 0
while opcao_menu != 3:
    opcao_menu = menu()
    # Caso o usuário escolha cadastrar uma novo usuário
    if opcao_menu == 1:
        while True:
            nick = input("\033[1mEntre com o seu nick: \033[m")
            # Verificando se o nome digitado é valido
            if nick.strip().isidentifier():
                nick = nick.strip()
                # Verificando se o login digitado existe no arquivo informado
                if login_existe(nick, NOME_ARQUIVO):
                    print("\033[1;31mO nick informado já está cadastrado no sistema \033[1m")
                    print("\033[1;31mPor favor, tente outro nick \033[m")
                    congelar_tela()
                else:
                    senha = input("\033[1mEntre com a sua senha: \033[m")
                    break
            # Caso o nick não seja válido
            else:
                print("\033[1;31mNick inválido \033[m")
                print("\033[1;31mO seu nick deve ser composto somente por caracteres alfanumericos e underline \033[m")
                congelar_tela()
        print("\033[1;31mCadastrando...\033[m")
        print("\033[1;31mUsuario cadastrado com sucesso!\033[m")
        # Instanciando o objeto do tipo usuário
        new_user = Usuario(nick, senha)
        # Cadastrando o usuário no sistema
        cadastrar_usuario(new_user, NOME_ARQUIVO)
        congelar_tela()

    # Caso o usuário escolha logar no sistema
    elif opcao_menu == 2:
        while True:
            login = input("\033[1mDigite o seu login: \033[m")
            senha = getpass("\033[1mDigite a sua senha: \033[m")
            print("\033[1;31mLogando no sistema... \033[m")
            # Autenticando o usuário no sistema
            if autenticar_usuario(login, senha, NOME_ARQUIVO):
                print("\033[1;31mLogin realizado com sucesso! \033[m")
                congelar_tela()
                opcao_sub_menu = sub_menu()
                while 5 != opcao_sub_menu:
                    # Caso o usuário escolha criar uma nova tarefa
                    if opcao_sub_menu == 1:
                        # Pedindo as informações da tarefa
                        titulo_tarefa = input("\033[1mTitulo da tarefa: \033[m")
                        descricao_tarefa = input("\033[1mDescricao da tarefa: \033[m")
                        prioridade_tarefa = menu_prioridade_tarefa()
                        # Instanciando o objeto da classe Tarefa
                        new_tarefa = Tarefa(titulo_tarefa, descricao_tarefa, prioridade_tarefa)
                # Caso o usuário saia da conta
                print("\033[1mDeslogando da conta... \033[m")
                print('\033[1mAguarde... \033[m')
                congelar_tela()
                break
            # Caso o login e/ou senha incorretos
            else:
                print("\033[1;31mLogin e/ou senha incorretos! \033[m")
print("\033[1mSaindo do programa... \033[1m")
congelar_tela()
