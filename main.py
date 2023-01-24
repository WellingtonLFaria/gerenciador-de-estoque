# Script principal, onde o usuário interage com o gerenciador de estoque

from estoque import *
from interface import *

estoque = Estoque()

while True:
    titulo('Gerenciador de Estoque')
    estoque.mostrar_produtos()
    linha()
    menu_de_opcoes(['Adicionar produto', 'Remover produto', 'Editar produto'])
    linha()
    while True:
        try:
            opcao = int(input())
            break
        except ValueError:
            print('Insira um valor válido.')
    linha()
    if opcao == 1:
        while True:
            try:
                nome = str(input('Nome do Produto: '))
                break
            except ValueError:
                print('Insira uma valor válido.')
        while True:
            try:
                descricao = str(input('Descrição do Produto: '))
                break
            except ValueError:
                print('Insira uma valor válido.')
        while True:
            try:
                preco_str = str(input('Preço do Produto(R$): '))
                preco = float(preco_str.replace(',', '.'))
                break
            except ValueError:
                print('Insira uma valor válido.')
        while True:
            try:
                quantidade = int(input('Quantidade do mesmo produto: '))
                break
            except ValueError:
                print('Insira um valor válido.')
        try:
            estoque.adicionar_produto(nome, descricao, preco, quantidade)
        except NameError:
            print('Cadastro de produto não realizado, valores incorretos.')
    
    elif opcao == 2:
        try:
            indice = int(input('Informe o índice do produto que deseja remover: '))
        except ValueError:
            print('Insira um valor válido.')
        estoque.remover_produto(indice)
    
    elif opcao == 3:
        try:
            indice = int(input('Informe o índice do produto que deseja editar: '))
        except ValueError:
            print('Insira um valor válido.')
        estoque.editar_produto(indice)
