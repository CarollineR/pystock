from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = request.form["quantidade"]
        print(nome)
        print(quantidade)
        
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)

