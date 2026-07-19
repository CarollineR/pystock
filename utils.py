# FUNÇÕES AUXILIARES

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


def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu principal: ")
