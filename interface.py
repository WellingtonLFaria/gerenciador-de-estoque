# Script que realiza todos os processos relacionados a criação de interface gráfica para o terminal
def linha(tamanho_da_linha=50):
    print(f'-'*(tamanho_da_linha))


def menu_de_opcoes(lista_de_opcoes):
    for c in range(0, len(lista_de_opcoes)):
        print(f'[{c+1}] {lista_de_opcoes[c]}')


def titulo(conteudo=''):
    tamanho_titulo = len(conteudo)
    linha(tamanho_da_linha=tamanho_titulo+2)
    print(f' {conteudo}')
    linha(tamanho_da_linha=tamanho_titulo+2)
