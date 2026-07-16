import json

produtos = [ ]

def carregar_produtos():
   global produtos

   with open("produtos.json", "r") as arquivo_json:
       produtos = json.load(arquivo_json)


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
    salvar_produtos()
    voltar_ao_menu()


def listar_produtos():
    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        return
    
    print("\n Produtos cadastrados:\n")

    for produto in produtos:
        print(f"\n Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")
    voltar_ao_menu()
    

def entrada_de_estoque():
    nome = input("Produto: ")

    for produto in produtos:

        if produto["nome"] == nome:
            quantidade = int(input("Quantidade: "))
            produto ["quantidade"] += quantidade
            salvar_produtos()
            print("Estoque atualizado!")
            voltar_ao_menu()
            return
        
    print("Produto não encontrado.")
    voltar_ao_menu()
    

def saida_de_estoque():
    nome = input("Produto: ")

    for produto in produtos:

        if produto["nome"] == nome:
            quantidade = int(input("Digite a quantidade que deseja retirar: "))

            if produto["quantidade"] < quantidade:
                print("Estoque insuficiente")
            else:
                produto["quantidade"] -= quantidade
                salvar_produtos()
                print("Saída realizada")
                print(f"Estoque de {produto['nome']} é de {produto['quantidade']} unidade(s)")

            voltar_ao_menu()
            return

    print("Produto não encontrado.")
    voltar_ao_menu()

def salvar_produtos():
    with open("produtos.json", "w") as arquivo_json:
        json.dump(produtos, arquivo_json, indent=4)


def sair():
    print('Encerrando...')

def opcao_invalida():
    print('Opção inválida\n!')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')


def escolher_opcoes():
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrar_produto()
        return True
    elif opcao == 2:
        listar_produtos()
        return True
    elif opcao == 3:
        entrada_de_estoque()
        return True
    elif opcao == 4:
        saida_de_estoque()
        return True
    elif opcao == 5:
        sair()
        return False
    else:
        opcao_invalida()
        voltar_ao_menu()
        return True


def main():
    carregar_produtos()
    exibir_nome_do_programa()
    while True: 
        exibir_opcoes()

        continuar = escolher_opcoes()
        
        if not continuar:
            break

if __name__ == "__main__":
    main()


    



