import json

produtos = [ ]


# FUNÇÕES AUXILIARES

def carregar_produtos():
   global produtos

   try:
       with open("produtos.json", "r") as arquivo_json:
           produtos = json.load(arquivo_json)
    
   except FileNotFoundError:
       produtos = []


def salvar_produtos():
    with open("produtos.json", "w") as arquivo_json:
        json.dump(produtos, arquivo_json, indent=4, ensure_ascii=False)


def ler_inteiro(mensagem):
    while True:
        valor = input(mensagem)
        
        try:
            valor = int(valor)

            if valor < 0:
                print("Digite um valor maior ou igual a zero.")
                continue

            return valor

        except ValueError:
            print("Digite um número válido.")

def ler_inteiro_positivo(mensagem):
    while True:
        valor = ler_inteiro(mensagem)

        if valor == 0:
            print("Digite um valor maior que zero.")
            continue

        return valor


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor.title()
        
        print("O campo não pode ficar vazio")


def deseja_repetir(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta == "s":
            return True
        
        if resposta == "n":
            return False
        
        print("Digite apenas 's' ou 'n'.")


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


def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu principal: ")


def sair():
    print("Encerrando...")


def opcao_invalida():
    print("Opção inválida!")


# FUNCIONALIDADES DO ESTOQUE

def cadastrar_produto():
   while True:
        nome = ler_texto("Digite o nome do produto: ")

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                print("Este produto já existe.")
                voltar_ao_menu()
                return
        
        quantidade = ler_inteiro("Digite a quantidade disponível: ")

        produto = {
            "nome": nome,
            "quantidade": quantidade
    }
        
        produtos.append(produto)
        salvar_produtos()
        print(f"Produto {nome} cadastrado com sucesso!")

        if not deseja_repetir("\nDeseja cadastrar outro produto? (s/n): "):
            voltar_ao_menu() 
            return   


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        voltar_ao_menu()
        return
    
    print("\n Produtos cadastrados:\n")

    total_unidades = 0

    for produto in produtos:
        print(f"\n Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")
        total_unidades += produto["quantidade"]

    print("\n------------------------------")
    print(f"Total de produtos: {len(produtos)}")
    print(f"Total de unidades em estoque: {total_unidades}")
    voltar_ao_menu()


def buscar_produto():
    nome_busca = input("Digite o nome do produto: ").strip()

    for produto in produtos:
        if produto["nome"].lower() == nome_busca.lower():
            print("\nProduto encontrado: ")
            print(f"Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")
            voltar_ao_menu()
            return
        
    print("Produto não encontrado.")
    voltar_ao_menu()
    

def entrada_de_estoque():
    while True:
        nome = ler_texto("Produto: ")
        encontrado = False

        for produto in produtos:

            if produto["nome"].lower() == nome.lower():
                encontrado = True

                quantidade = ler_inteiro_positivo("Quantidade: ")
                produto["quantidade"] += quantidade
                salvar_produtos()

                print("Entrada de estoque realizada com sucesso!")
                print(f"Estoque atual de {produto['nome']}: {produto['quantidade']} unidade(s).")

                if not deseja_repetir("\nDeseja registrar outra entrada? (s/n): "):
                    voltar_ao_menu()
                    return
            
                break

        if not encontrado:
            print("Produto não encontrado.")

            if not deseja_repetir("\nDeseja tentar outro produto? (s/n): "):
                voltar_ao_menu()
                return
        

def saida_de_estoque():
    while True:
        nome = ler_texto("Produto: ")
        encontrado = False

        for produto in produtos:

            if produto["nome"].lower() == nome.lower():
                encontrado = True

                quantidade = ler_inteiro_positivo("Digite a quantidade que deseja retirar: ")

                if produto["quantidade"] < quantidade:
                    print("Estoque insuficiente.")
                else:
                    produto["quantidade"] -= quantidade
                    salvar_produtos()

                    print("Saída de estoque realizada com sucesso!")
                    print(f"Estoque atual de {produto['nome']}: {produto['quantidade']} unidade(s).")

                if not deseja_repetir("\nDeseja registrar outra saída? (s/n): "):
                    voltar_ao_menu()
                    return
                
                break

        if not encontrado:
            print("Produto não encontrado.")

            if not deseja_repetir("\nDeseja tentar outro produto? (s/n): "):
                voltar_ao_menu()
                return


def excluir_produto():
   while True:
        nome = ler_texto("Digite o nome do produto: ")
        encontrado = False

        for produto in produtos:

            if produto["nome"].lower() == nome.lower():
                encontrado = True

                print("\nProduto encontrado:")
                print(f"Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")

                confirmacao = input("Deseja realmente excluir este produto? (s/n): ").strip().lower()

                if confirmacao == "s":
                    produtos.remove(produto)
                    salvar_produtos()
                    print("Produto excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")

                if not deseja_repetir("\nDeseja excluir outro produto? (s/n): "):
                    voltar_ao_menu()
                    return
                
                break

        if not encontrado:
            print("Produto não encontrado.")

            if not deseja_repetir("\nDeseja tentar outro produto? (s/n): "):
                voltar_ao_menu()
                return
    

# CONTROLE DO MENU

def escolher_opcoes():
    opcao = ler_inteiro("Digite a opção desejada: ")
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
        buscar_produto()
        return True
    elif opcao == 6:
        excluir_produto()
        return True
    elif opcao == 7:
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


    



