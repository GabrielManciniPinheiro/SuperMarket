# Importando bibliotecas necessárias
import mysql.connector
from mysql.connector import Error
from tkinter import *
# Criando conexão com o banco de dados
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        database='codes',
        user='root',
        password='12345')

    if connection.is_connected():
        print('Conexão bem-sucedida.')
except Error as e:
    print('Erro ao conectar:', e)

# Criando a interface gráfica usando o módulo tkinter
root = Tk()
root.title('Supermercado')

# Adicionando widgets para a inserção de novos produtos no estoque
Label(root, text='Produto:').grid(row=0, column=0)
entrada_produto = Entry(root)
entrada_produto.grid(row=0, column=1)

Label(root, text='Preço:').grid(row=1, column=0)
entrada_preco = Entry(root)
entrada_preco.grid(row=1, column=1)

Label(root, text='Quantidade:').grid(row=2, column=0)
entrada_quantidade = Entry(root)
entrada_quantidade.grid(row=2, column=1)

def inserir_produto():
    produto = entrada_produto.get()
    preco = entrada_preco.get()
    quantidade = entrada_quantidade.get()
    inserir_produto_no_banco_de_dados(produto, preco, quantidade)
    entrada_produto.delete(0, END)
    entrada_preco.delete(0, END)
    entrada_quantidade.delete(0, END)

botao_inserir = Button(root, text='Inserir', command=inserir_produto)
botao_inserir.grid(row=3, column=0, columnspan=2)

# Criando uma tabela para armazenar o estoque
try:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS estoque ('
                   'id INT AUTO_INCREMENT PRIMARY KEY,'
                   'produto VARCHAR(255),'
                   'preco DECIMAL(10, 2),'
                   'quantidade INT)')
    print('Tabela criada com sucesso.')
except Error as e:
    print('Erro ao criar tabela:', e)

# Criando funções para inserir, atualizar e excluir produtos do estoque
def inserir_produto_no_banco_de_dados(produto, preco, quantidade):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO estoque (produto, preco, quantidade) VALUES (%s, %s, %s)"
        values = (produto, preco, quantidade)
        cursor.execute(query, values)
        connection.commit()
        print(f'{cursor.rowcount} produto(s) inserido(s) com sucesso.')
    except Error as e:
        print('Erro ao inserir produto:', e)

def atualizar_produto(id, produto, preco, quantidade):
    try:
        cursor = connection.cursor()
        query = "UPDATE estoque SET produto=%s, preco=%s, quantidade=%s WHERE id=%s"
        values = (produto, preco, quantidade, id)
        cursor.execute(query, values)
        connection.commit()
        print(f'{cursor.rowcount} produto(s) atualizado(s) com sucesso.')
    except Error as e:
        print('Erro ao atualizar produto:', e)

def excluir_produto(id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM estoque WHERE id=%s"
        values = (id,)
        cursor.execute(query, values)
        connection.commit()
        print(f'{cursor.rowcount} produto(s) excluído(s) com sucesso.')
    except Error as e:
        print('Erro ao excluir produto:', e)

# Adicionando widgets para atualização e exclusão de produtos do estoque

Label(root, text='ID do produto:').grid(row=4, column=0)
entrada_id = Entry(root)
entrada_id.grid(row=4, column=1)

Label(root, text='Nome do produto:').grid(row=5, column=0)
entrada_novo_produto = Entry(root)
entrada_novo_produto.grid(row=5, column=1)

Label(root, text='Novo preço:').grid(row=6, column=0)
entrada_novo_preco = Entry(root)
entrada_novo_preco.grid(row=6, column=1)

Label(root, text='Nova quantidade:').grid(row=7, column=0)
entrada_nova_quantidade = Entry(root)
entrada_nova_quantidade.grid(row=7, column=1)

def atualizar_produto_gui():
    id = entrada_id.get()
    produto = entrada_novo_produto.get()
    preco = entrada_novo_preco.get()
    quantidade = entrada_nova_quantidade.get()
    atualizar_produto(id, produto, preco, quantidade)
    entrada_id.delete(0, END)
    entrada_novo_produto.delete(0, END)
    entrada_novo_preco.delete(0, END)
    entrada_nova_quantidade.delete(0, END)

botao_atualizar = Button(root, text='Atualizar', command=atualizar_produto_gui)
botao_atualizar.grid(row=8, column=0, columnspan=2)

def excluir_produto_gui():
    id = entrada_id.get()
    excluir_produto(id)
    entrada_id.delete(0, END)

botao_excluir = Button(root, text='Excluir', command=excluir_produto_gui)
botao_excluir.grid(row=9, column=0, columnspan=2)

# Mostrando os produtos do estoque na interface gráfica

try:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM estoque')
    produtos = cursor.fetchall()
    for i, produto in enumerate(produtos):
        Label(root, text=f'{produto[1]} (R${produto[2]:.2f}) - {produto[3]} unidades').grid(row=i+10, column=0, columnspan=2)
except Error as e:
    print('Erro ao mostrar produtos:', e)

root.mainloop()

# Fechando conexão com o banco de dados

if connection.is_connected():
    connection.close()
    print('Conexão encerrada.')













