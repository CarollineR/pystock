produtos = [ ]

def exibir_nome_do_programa():
    print("""
====================
      PYSTOCK
====================
""")


def exibir_opcoes():
    print('1. Cadastrar Produto')
    print('2. Listar Produtos')
    print('3. Entrada de Estoque')
    print('4. Saída de Estoque')
    print('5. Sair')

def cadastrar_produto():
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade disponível: '))
    produto = {
        "nome": nome,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso!")
    voltar_ao_menu()

def listar_produtos():
    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        return
    for produto in produtos:
        print("\n Produtos cadastrados:\n")
        print(f"\n Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")
        voltar_ao_menu()
    

def entrada_de_estoque():
    print('Entrada de Estoque')

def saida_de_estoque():
    print('Saída de Estoque')

def sair():
    print('Saindo')

def opcao_invalida():
    print('Opção inválida\n!')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')


def escolher_opcoes():
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        entrada_de_estoque()
    elif opcao == 4:
        saida_de_estoque()
    elif opcao == 5:
        sair()
    else:
        opcao_invalida()
        voltar_ao_menu()


def main():
    exibir_nome_do_programa()
    while True: 
        exibir_opcoes()
        escolher_opcoes()

if __name__ == "__main__":
    main()





    
    



