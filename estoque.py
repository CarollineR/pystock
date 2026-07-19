import database
import utils

# FUNCIONALIDADES DO ESTOQUE

def cadastrar_produto():
   while True:
        nome = utils.ler_texto("Digite o nome do produto: ")

        for produto in database.produtos:
            if produto["nome"].lower() == nome.lower():
                print("Este produto já existe.")
                utils.voltar_ao_menu()
                return
        
        quantidade = utils.ler_inteiro("Digite a quantidade disponível: ")

        produto = {
            "nome": nome,
            "quantidade": quantidade
    }
        
        database.produtos.append(produto)
        database.salvar_produtos()
        print(f"Produto {nome} cadastrado com sucesso!")

        if not utils.deseja_repetir("\nDeseja cadastrar outro produto? (s/n): "):
            utils.voltar_ao_menu() 
            return   


def listar_produtos():
    if not database.produtos:
        print("Nenhum produto cadastrado.")
        utils.voltar_ao_menu()
        return
    
    print("\n Produtos cadastrados:\n")

    total_unidades = 0

    for produto in database.produtos:
        print(f"\n Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")
        total_unidades += produto["quantidade"]

    print("\n------------------------------")
    print(f"Total de produtos: {len(database.produtos)}")
    print(f"Total de unidades em estoque: {total_unidades}")
    utils.voltar_ao_menu()


def buscar_produto():
    nome_busca = input("Digite o nome do produto: ").strip()

    for produto in database.produtos:
        if produto["nome"].lower() == nome_busca.lower():
            print("\nProduto encontrado: ")
            print(f"Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")
            utils.voltar_ao_menu()
            return
        
    print("Produto não encontrado.")
    utils.voltar_ao_menu()
    

def entrada_de_estoque():
    while True:
        nome = utils.ler_texto("Produto: ")
        encontrado = False

        for produto in database.produtos:

            if produto["nome"].lower() == nome.lower():
                encontrado = True

                quantidade = utils.ler_inteiro_positivo("Quantidade: ")
                produto["quantidade"] += quantidade
                database.salvar_produtos()

                print("Entrada de estoque realizada com sucesso!")
                print(f"Estoque atual de {produto['nome']}: {produto['quantidade']} unidade(s).")

                if not utils.deseja_repetir("\nDeseja registrar outra entrada? (s/n): "):
                    utils.voltar_ao_menu()
                    return
            
                break

        if not encontrado:
            print("Produto não encontrado.")

            if not utils.deseja_repetir("\nDeseja tentar outro produto? (s/n): "):
                utils.voltar_ao_menu()
                return
        

def saida_de_estoque():
    while True:
        nome = utils.ler_texto("Produto: ")
        encontrado = False

        for produto in database.produtos:

            if produto["nome"].lower() == nome.lower():
                encontrado = True

                quantidade = utils.ler_inteiro_positivo("Digite a quantidade que deseja retirar: ")

                if produto["quantidade"] < quantidade:
                    print("Estoque insuficiente.")
                else:
                    produto["quantidade"] -= quantidade
                    database.salvar_produtos()

                    print("Saída de estoque realizada com sucesso!")
                    print(f"Estoque atual de {produto['nome']}: {produto['quantidade']} unidade(s).")

                if not utils.deseja_repetir("\nDeseja registrar outra saída? (s/n): "):
                    utils.voltar_ao_menu()
                    return
                
                break

        if not encontrado:
            print("Produto não encontrado.")

            if not utils.deseja_repetir("\nDeseja tentar outro produto? (s/n): "):
                utils.voltar_ao_menu()
                return


def excluir_produto():
   while True:
        nome = utils.ler_texto("Digite o nome do produto: ")
        encontrado = False

        for produto in database.produtos:

            if produto["nome"].lower() == nome.lower():
                encontrado = True

                print("\nProduto encontrado:")
                print(f"Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")

                confirmacao = input("Deseja realmente excluir este produto? (s/n): ").strip().lower()

                if confirmacao == "s":
                    database.produtos.remove(produto)
                    database.salvar_produtos()
                    print("Produto excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")

                if not utils.deseja_repetir("\nDeseja excluir outro produto? (s/n): "):
                    utils.voltar_ao_menu()
                    return
                
                break

        if not encontrado:
            print("Produto não encontrado.")

            if not utils.deseja_repetir("\nDeseja tentar outro produto? (s/n): "):
                utils.voltar_ao_menu()
                return