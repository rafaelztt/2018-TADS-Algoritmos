# Importa uma biblioteca para poder usar seu conteúdo
import sqlite3

########### F U N Ç Õ E S #########

def criar_tabela_usuario(conexao):

    # Cria o cursor para operar o banco
    cursor = conexao.cursor()

    # Monta o SQL a ser executado
    sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            nome text,
            login text,
            senha text
        );
    """

    # Executa um SQL
    cursor.execute(sql)

# Inserir novo usuário
def inserir_usuario(conexao):

    # Cria o cursos para operar o banco
    cursor = conexao.cursor()

    # Pede os dados para o usuário
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    # Monta o select com o format e os dados
    sql = """
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    """.format(nome, login, senha)

    # Exemplo:
    # sql = """
    #     INSERT INTO usuario VALUES(
    #         'Rafael Zottesso',
    #         'rafael',
    #         '123'
    #     );
    # """

    # Executa o sql
    cursor.execute(sql)

    # Salvar as modificações.
    # O commit sempre deve ser feito depois do INSERT, UPDATE ou DELETE
    conexao.commit()


############ P R I N C I P A L #############

# 1º - Iniciar a conexão (ligação) com nosso banco
conexao = sqlite3.connect("aula28.sqlite")


inserir_usuario(conexao)



# Fechando a conexão (ligação) com o banco
conexao.close()
