import json

ARQUIVO = "produtos.json"

produtos = [ ]

def carregar_produtos():
   global produtos

   try:
       with open("ARQUIVO", "r") as arquivo_json:
           produtos = json.load(arquivo_json)
    
   except FileNotFoundError:
       produtos = []


def salvar_produtos():
    with open("ARQUIVO", "w") as arquivo_json:
        json.dump(produtos, arquivo_json, indent=4, ensure_ascii=False)
