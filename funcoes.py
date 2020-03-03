from hashlib import sha512
from os import getcwd, chdir, system, name, mkdir
from os import path, sep, listdir
from pickle import dump, load
from time import sleep
from Tarefa import *
from Usuario import *
'''
sep é o caractere usado pelo SO para diferenciar pastas de arquivos
'''
# Nome do diretório que irá armazenar as tarefas dos usuários
NOME_DIRETORIO_TAREFAS = "tarefas"
# Caminho onde o script se encontra
CAMINHO_SCRIPT = getcwd()


# Tem como parâmetro uma string
# Aplica a função hashing sha512 a string e retorna o digest
# Retorna uma hash SHA512 da senha em forma hexadecimal
def encriptar(senha: str) -> object:
    digest = sha512()
    digest.update(senha.encode('utf-8'))
    return digest.hexdigest()


# Limpa a tela do computador (funciona em linux e windows)
# Retorna None
def limpar_tela() -> None:
    system('cls' if name == 'nt' else 'clear')
    return None


'''# Identifica o SO que roda na máquina do usuário
# Retorna 1 se o sistema for windows
# e -1 caso contrário
def identificar_SO() -> int:
    tipo_SO = name
    return 1 if tipo_SO == 'nt' else -1'''


# Não há parâmetro
# A função lê um inteiro, ou seja, ela obriga o usuário
# a digitar um valor do tipo inteiro
# Retorna o valor digitado
def ler_inteiro() -> int:
    while True:
        try:
            inteiro = int(input('> '))
            return inteiro
        except ValueError:
            pass


# Menu principal do sistema
# Exibe as opções para o usuário
# Retorna a função ler_inteiro
# Porém coloquei que retorna um inteiro pois a
# a função leia_inteiro retorna um inteiro
def menu() -> int:
    limpar_tela()
    print('_' * 33)
    print()
    print("|     GERENCIADOR DE TAREFAS    |")
    print('_' * 33)
    print()
    print("[ 1 ] - Cadastrar novo usuario")
    print('[ 2 ] - Logar no sistema')
    print("[ 3 ] - Sair do sistema")
    return ler_inteiro()


# Exibe as opções disponíveis para
# os usuários logados no sistema
# Retorna a função ler_inteiro
def sub_menu() -> int:
    limpar_tela()
    print("[ 1 ] - Cadastrar nova Tarefa")
    print("[ 2 ] - Visualizar Tarefas")
    print("[ 3 ] - Alterar Tarefa")
    print("[ 4 ] - Excluir Tarefa")
    print("[ 5 ] - Sair")
    return ler_inteiro()


# Exibe o mini menu da prioridade da tarefa a cadastrada
# Retorna a função ler_inteiro
# Porém coloquei que retorna um inteiro pois a
# a função leia_inteiro retorna um inteiro
def menu_prioridade_tarefa() -> int:
    print("\033[1m  PRIORIDADE DA TAREFA\033[m")
    print("[ 1 ] - Prioridade Baixa")
    print("[ 2 ] - Prioridade Media")
    print("[ 3 ] - Prioridade ALta")
    return ler_inteiro()


# Não possui parâmetros
# Congela a tela durante 4.2 segundos
# Retrona None
def congelar_tela() -> None:
    sleep(4.2)
    return None


# Tem como parâmetro, três strings, senha do usuário, nome do
# usuário e o nome do arquivo a ser manipulado
# Autentica o usuário no sistema
# Retorna True caso o usuário for autenticado com sucesso
# e False caso contrário
def autenticar_usuario(login: str, senha: str, nome_arq: str) -> bool:
    # Abrindo o arquivo que guarda os usuários
    with open(nome_arq) as arquivo:
        # Iterando o arquivo
        for linha in arquivo:
            # Removendo o \n da linha encontrada e desemenbrando a linha
            linha = linha[:-1].split(' ')
            # Verificando se o login e senha digitados estão corretos
            if login == linha[0] and linha[1] == encriptar(senha):
                return True
        # Caso o login e senha digitados não estejam corretos
        return False


# Tem como parâmetro duas strings, o nome do arquivo a ser verificado
# e o caminho a ser verificado, por padrão ele tem como valor o caminho
# atual do arquivo .py
# Verifica se um arquivo existe, pelo nome
# Retorna True caso o arquivo exista, e False caso não
def arquivo_existe(nome_arq: str, caminho: str = getcwd()) -> bool:
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


'''# Tem como parâmetro uma string, o nome do usuário
# Verifica se a string é "nula", se o login é composto
# somente por caracter nulo, também verifica se há
# caracteres em branco no nome, além de eliminar os caracteres em
# branco do nome (a esquerda e a direita do nome)
# Retorna True caso a string seja "válida" e False caso não
def validar_nome(nome: str) -> bool:
    # Stripando a string, tirando os espaços ao redor
    nome = nome.strip()
    # Verificando se a string é "nula"
    if nome:
        for caractere in nome:
            # Verificando se a string de 8 bits é um espaço
            if caractere.isspace():
                return False
        # Caso não encontre nenhum caractere "em branco"
        return True
    # Caso a string seja "nula"
    return False
'''


# Tem como parâmetro uma string, o nome do arquivo
# e um inteiro, o tipo do arquivo, respectivamente.
# Para o tipo do arquivo: 0- simboliza arquivo
# em modo de texto e qualquer numero diferente
# de 0 simboliza o arquivo em modo binário
# Cria um arquivo de texto ou binário
# Retorna 1 caso o arquivo foi criado com sucesso
# Retorna 0 caso o arquivo já exista
def criar_arquivo(nome_arq: str, tipo_arq: int, caminho=getcwd()) -> int:
    # Caminho onde o script se localiza
    global CAMINHO_SCRIPT
    # Mudando de diretório informado pelo usuário
    chdir(caminho)
    try:
        # Criando o arquivo
        arquivo = open(nome_arq, 'x') if tipo_arq == 0 else open(nome_arq, 'xb')
        arquivo.close()
        return 1
    except FileExistsError:
        pass
    finally:
        chdir(CAMINHO_SCRIPT)
    return 0


# Tem como parâmetro uma lista do tipo list
# Ordena a lista de acordo com a prioridade                     # PRECISO DEFINIR EM QUE POSIÇÃO VAI FICAR O VALOR QUE SIMBOLIZA A PRIORIDADE, ACREDITO QUE SERÁ LOGO NA PRIMEIRA
# Retorna a lista ordenada
def ordenar_tarefa(lista: list):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


# Tem como parâmetro um objeto do tipo Usuario e uma string
# o nome do arquivo no qual as informações vão ser gravadas
# Cadastra um usuário no sistema, melhor dizendo, insere
# o nome e senha do usuário no arquivo em modo de texto que
# guarda todos os usuários do sistema
def cadastrar_usuario(usuario: Usuario, nome_arq: str) -> bool:
    # Gravando o nome e o hash da senha do usuário no arquivo "nome_arq"
    with open(nome_arq, 'a', encoding='utf-8') as arquivo:
        arquivo.write(usuario.get_nome() + " " + encriptar(usuario.get_senha()) + '\n')
    # Criando o diretório com o nome do usuário e que irá guardar suas tarefas
    criar_diretorio(usuario.get_nome(), CAMINHO_SCRIPT + sep + NOME_DIRETORIO_TAREFAS)
    # Caminho onde o arquivo binário será criado
    caminho_arq_binario = CAMINHO_SCRIPT + sep + NOME_DIRETORIO_TAREFAS + sep + usuario.get_nome() + sep
    # Criando o arquivo em modo binário que guarda as tarefas do usuário
    criar_arquivo(usuario.get_nome() + "_tarefas.pbl", 1, caminho_arq_binario)
    # Criando o arquivo em modo binário que guarda a ultima ocorrência do ID da tarefa
    criar_arquivo(usuario.get_nome() + ".i", 1, caminho_arq_binario)
    # Mudando para o diretório onde se encontra o arquivo binário ".i"
    chdir(CAMINHO_SCRIPT + sep + NOME_DIRETORIO_TAREFAS + sep + usuario.get_nome())
    append_b(0, usuario.get_nome() + ".i")
    # Voltando para o diretório do script
    chdir(CAMINHO_SCRIPT)
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


'''# Tem como parâmetro uma string
# Remove os caracteres barra string
# Retorna a string sem os caracteres barra
def remover_barra(texto: str) -> str:
    # Contador de barras da string
    contador_barras = texto.count('/')
    # Convertendo a string para lista
    texto = list(texto)
    # Removendo as barras da string
    for i in range(contador_barras):
        texto.remove('/')
    # Convertendo a lista para string
    texto = ''.join(texto)
    return texto


# Tem como parâmetro uma string
# Remove os caracteres contra-barra da string
# Retorna a string sem os caracteres contra barra
def remover_contra_barra(texto: str) -> str:
    # Contador de contra-barras da string
    contador_contra_barra = texto.count('\\')
    # Convertendo a string para lista
    texto = list(texto)
    # Removendo as contra-barras da string
    for i in range(contador_contra_barra):
        texto.remove('\\')
    # Convertendo a lista para string
    texto = ''.join(texto)
    return texto
'''


# Tem como parâmetro uma string, o nome do arquivo a ser lido
# A função trabalha somente com arquivo .dat
# Lê um arquivo binário e retorna uma tupla contendo as linhas
# do arquivo, cada linha é um item da tupla.
def read_b(nome_arq: str) -> tuple:
    linhas = []
    # Abrindo o arquivo para leitura
    arquivo = open(nome_arq, 'rb')
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
    arquivo = open(nome_arq, "ab")
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
        global CAMINHO_SCRIPT
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
            chdir(CAMINHO_SCRIPT)
        return 0
    # Caso o nome do diretório seja uma string nula
    return 0


# Tem como parâmetro uma string (nome do usuário, e tarefa
# do tipo tarefa
# Cadastra uma nova tarefa no usuário passado como argumento
def cadastrar_tarefa(tarefa: Tarefa, nome_usuario: str) -> bool:
    global CAMINHO_SCRIPT
    caminho_padrao = getcwd()
    caminho_arq_binario = getcwd() + sep + NOME_DIRETORIO_TAREFAS + sep + nome_usuario + sep
    # Mudando para o diretório onde se encontra o arquivo do usuário
    chdir(caminho_arq_binario)
    append_b(1, nome_usuario + '_tarefas.pbl')
    # Voltando para o diretório onde o script está
    chdir(caminho_padrao)
    return True
