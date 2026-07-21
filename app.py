from flask import Flask, render_template, request
import json

app = Flask(__name__)

ARQUIVO = "produtos.json"

def carregar_produtos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    

def salvar_produtos(produtos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    lista_produtos = carregar_produtos()

    return render_template(
        "produtos.html",
        produtos=lista_produtos
    )

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = int(request.form["quantidade"])

        produtos = carregar_produtos()

        novo_produto = {
            "nome": nome,
            "quantidade": quantidade
        }

        produtos.append(novo_produto)

        salvar_produtos(produtos)
        
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)

