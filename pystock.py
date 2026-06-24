def exibir_nome_do_programa():
    print("""
====================
      PYSTOCK
====================
""")

exibir_nome_do_programa()

opcao = 0

while opcao != 5:
    print('1. Cadastrar Produto')
    print('2. Listar Produtos')
    print('3. Entrada de Estoque')
    print('4. saída de Estoque')
    print('5. Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('Cadastrar Produto')

    elif opcao == 2:
        print('Listar Produtos')

    elif opcao == 3:
        print('Entrada de Estoque')

    elif opcao == 4:
        print('Saída de Estoque')

    elif opcao == 5:
        print('Saindo')

    else:
        print('Opção Inválida')



