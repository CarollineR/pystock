from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)

app.secret_key = "pystock-chave"

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
        nome = request.form["nome"].strip().title()

        try:
            quantidade = int(request.form["quantidade"])
        except ValueError:
            flash("Digite uma quantidade válida.")
            return redirect("/cadastro")
        
        if quantidade < 0:
            flash("A quantidade não pode ser negativa.")
            return redirect("/cadastro")

        if not nome:
            flash("O nome do produto é obrigatório.")
            return redirect("/cadastro")

        produtos = carregar_produtos()

        for produto_existente in produtos:
            if produto_existente["nome"].lower() == nome.lower():
                flash("Este produto já está cadastrado.")
                return redirect("/cadastro")

        novo_produto = {
            "nome": nome,
            "quantidade": quantidade
        }

        produtos.append(novo_produto)

        salvar_produtos(produtos)

        flash("Produto cadastrado com sucesso!")
        return redirect("/cadastro")
        
    return render_template("cadastro.html")


@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    if request.method == "POST":
        nome_busca = request.form["nome"].strip()

        if not nome_busca:
            flash("O nome do produto é obrigatório.")
            return redirect("/buscar")

        produtos = carregar_produtos()

        for produto in produtos:
            if produto["nome"].lower() == nome_busca.lower():
                return render_template(
                    "buscar.html",
                    produto=produto
                )

        flash("Produto não encontrado.")
        return redirect("/buscar")
    
    return render_template("buscar.html")

@app.route("/entrada", methods=["GET", "POST"])
def entrada():

    if request.method == "POST":

        nome = request.form["nome"].strip().title()

        try:
            quantidade = int(request.form["quantidade"])

            if quantidade < 0:
                flash("Digite uma quantidade válida")
                return redirect(url_for("entrada"))

            if quantidade == 0:
                flash("A quantidade deve ser maior que zero.")
                return redirect(url_for("entrada"))

        except ValueError:
            flash("Digite uma quantidade válida.")
            return redirect(url_for("entrada"))

        produtos = carregar_produtos()

        for produto in produtos:
            if produto["nome"] == nome:
                produto["quantidade"] += quantidade

                salvar_produtos(produtos)

                flash("Entrada de estoque registrada com sucesso!")
                return redirect(url_for("entrada"))

        flash("Produto não encontrado.")
        return redirect(url_for("entrada"))

    return render_template("entrada.html")


@app.route("/saida", methods=["GET", "POST"])
def saida():

    if request.method == "POST":

        nome = request.form["nome"].strip().title()

        try:
            quantidade = int(request.form["quantidade"])

            if quantidade < 0:
                flash("Digite uma quantidade válida.")
                return redirect(url_for("saida"))

            if quantidade == 0:
                flash("A quantidade deve ser maior que zero.")
                return redirect(url_for("saida"))

        except ValueError:
            flash("Digite uma quantidade válida.")
            return redirect(url_for("saida"))

        produtos = carregar_produtos()

        for produto in produtos:
            if produto["nome"] == nome:

                if quantidade > produto["quantidade"]:
                    flash("Quantidade insuficiente em estoque.")
                    return redirect(url_for("saida"))

                produto["quantidade"] -= quantidade

                salvar_produtos(produtos)

                flash("Saída de estoque registrada com sucesso.")
                return redirect(url_for("saida"))

        flash("Produto não encontrado.")
        return redirect(url_for("saida"))

    return render_template("saida.html")


@app.route("/excluir", methods=["GET", "POST"])
def excluir():

    if request.method == "POST":

        nome = request.form["nome"].strip().title()

        if not nome:
            flash("O nome do produto é obrigatório.")
            return redirect(url_for("excluir"))

        produtos = carregar_produtos()

        for produto in produtos:
            if produto["nome"] == nome:

                return render_template(
                    "confirmar_exclusao.html",
                    produto=produto
                )
        flash("Produto não encontrado.")
        return redirect(url_for('excluir'))

    return render_template("excluir.html")

@app.route("/confirmar_exclusao", methods=["POST"])
def confirmar_exclusao():

    nome = request.form["nome"]

    produtos = carregar_produtos()

    for produto in produtos:
        if produto["nome"] == nome:
            produtos.remove(produto)

            salvar_produtos(produtos)

            flash("Produto excluído com sucesso!")
            return redirect(url_for("excluir"))

    flash("Produto não encontrado.")
    return redirect(url_for("excluir"))


if __name__ == "__main__":
    app.run(debug=True)

