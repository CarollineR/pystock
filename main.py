import database
import estoque 
import utils

# FUNÇÕES DE APRESENTAÇÃO

def exibir_nome_do_programa():
    print("""
====================
      PYSTOCK
====================
""")


def exibir_opcoes():
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Entrada de Estoque")
    print("4. Saída de Estoque")
    print("5. Buscar Produto")
    print("6. Excluir Produto")
    print("7. Sair")


def sair():
    print("Encerrando...")


def opcao_invalida():
    print("Opção inválida!")


# CONTROLE DO MENU

def escolher_opcoes():
    opcao = utils.ler_inteiro("Digite a opção desejada: ")
    if opcao == 1:
        estoque.cadastrar_produto()
        return True
    elif opcao == 2:
        estoque.listar_produtos()
        return True
    elif opcao == 3:
        estoque.entrada_de_estoque()
        return True
    elif opcao == 4:
        estoque.saida_de_estoque()
        return True
    elif opcao == 5:
        estoque.buscar_produto()
        return True
    elif opcao == 6:
        estoque.excluir_produto()
        return True
    elif opcao == 7:
        sair()
        return False
    else:
        opcao_invalida()
        utils.voltar_ao_menu()
        return True


def main():
    database.carregar_produtos()
    exibir_nome_do_programa()
    while True: 
        exibir_opcoes()

        continuar = escolher_opcoes()
        
        if not continuar:
            break

if __name__ == "__main__":
    main()


    



