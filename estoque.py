# Script que fará todo o processo de manipulação dos dados do estoque

from interface import *

class Estoque():
    def __init__(self):
        self.produtos = []


    def adicionar_produto(self, nome, descricao, preco, quantidade):
        novo_produto = {'nome': nome, 'descrição' : descricao, 'preço' : preco, 'quantidade' : quantidade}
        self.produtos.append(novo_produto)
        print('Produto adicionado com sucesso!')


    def remover_produto(self, index_do_produto):
        try:
            self.produtos.pop(index_do_produto)
            print('Produto removido com sucesso!')
        except IndexError:
            print('Índice informado não existe.')


    def editar_produto(self, index_do_produto):
        try:
            print('O que deseja mudar: ')
            print(f'Nome do produto: {self.produtos[index_do_produto]["nome"]} | Descrição do produto: {self.produtos[index_do_produto]["descrição"]} | Preço do produto(R$): {self.produtos[index_do_produto]["preço"]:.2f} | Quantidade do mesmo produto: {self.produtos[index_do_produto]["quantidade"]}')
            menu_de_opcoes(['Nome', 'Descrição', 'Preço', 'Quantidade'])
            while True:
                try:
                    opcao = int(input())
                    break
                except ValueError:
                    print('Insira um valor válido.')
            
            if opcao == 1:
                while True:
                    try:
                        nome = str(input('Nome: '))
                        print('Nome do produto editado com sucesso!')
                        self.produtos[index_do_produto]['nome'] = nome
                        break
                    except ValueError:
                        print('Insira um valor válido.')
            elif opcao == 2:
                while True:
                    try:
                        descricao = str(input('Descrição: '))
                        print('Descrição do produto editado com sucesso!')
                        self.produtos[index_do_produto]['descrição'] = descricao
                        break
                    except ValueError:
                        print('Insira um valor válido.')
            elif opcao == 3:
                preco_str = str(input('Preço(R$): '))
                preco = float(preco_str.replace(',', '.'))
                print('Preço do produto editado com sucesso!')
                self.produtos[index_do_produto]['preço'] = preco
            
            elif opcao == 4:
                while True:
                    try:
                        quantidade = int(input('Quantidade do mesmo produto: '))
                        print('Quantidade do mesmo produto editada com sucesso!')
                        self.produtos[index_do_produto]['quantidade'] = quantidade
                        break
                    except ValueError:
                        print('Insira um valor válido.')
        except IndexError:
            print('Índice informado não existe.')


    def mostrar_produtos(self):
        titulo('Estoque Atual:')
        if len(self.produtos) == 0:
            print('Estoque vazio, nenhum produto foi cadastrado no estoque ainda.')
        else:
            for c in range(0, len(self.produtos)):
                print(f'[{c}] Nome do produto: {self.produtos[c]["nome"]} | Descrição do produto: {self.produtos[c]["descrição"]} | Preço do produto(R$): {self.produtos[c]["preço"]:.2f} | Quantidade do mesmo produto: {self.produtos[c]["quantidade"]}')
