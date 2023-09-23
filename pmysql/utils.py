import mysql.connector
from mysql.connector import errorcode


def conectar():
    """
    Função para conectar ao servidor
    """

    try:
        conn = mysql.connector.connect(
            user='luan',
            password='santiago',
            host='localhost',
            database='pmysql'
        ),
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Alguma coisa deu errado com seu nome ou senha , tente novamente')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Base de dados não existe')
        else:
            print(err)
    else:
        conn.close()


def desconectar():
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos ')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos.....')
        print('----------------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('----------------------')

    else:
        print('Não existem produtos cadastrados')
    desconectar(conn)


def inserir(conn=None):

    conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto:')
    preco = float(input('Informe o preço do ´produto:'))
    estoque = int(input('Informe a quantida em estoque: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}' , '{preco}', '{estoque}')")
    cursor.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso')
    else:
        print('Não foi possivel inserir o produto:')
    desconectar(conn)


def atualizar(conn=None):
    """
    Função para atualizar um produto
    """
    conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o codigo do produto:'))
    nome = input('Informe o novo nome do produto :')
    preco = float(input('Informe o novo preço do produto:'))
    estoque = int(input('Informe o novo número em estoque :'))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco= '{preco}', estoque='{estoque}', WHERE id='{codigo}'")
    cursor.commit()
    if cursor.rowcount == 1:
        print(f'O produto foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)


def deletar(conn=None):
    """
    Função para deletar um produto
    """
    conectar()
    cursor = conn.cursor()

    codigo = input(input('Informe o codigo do produto'))

    cursor.execute(f'DELETE FROM produtos WHRE id={codigo}')
    cursor.commit()

    if cursor.rowcount == 1:
        print(f'O produto foi deletado com sucesso')
    else:
        print('Erro ao deletar o produto.')


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')

