from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/ajuda")
def sobre():
    return render_template("paginas/ajuda.html", \
        titulo_pagina="Ajuda")
    
@app.route("/conta")
def sobre():
    return render_template("paginas/conta.html", \
        titulo_pagina="Conta")

@app.route("/extratodepontos")
def sobre():
    return render_template("paginas/extratodepontos.html", \
        titulo_pagina="Extrato de pontos")

@app.route("/ofertasespeciais")
def sobre():
    return render_template("paginas/ofertasespeciais.html", \
        titulo_pagina="Ofertas especiais")

@app.route("/premios")
def sobre():
    return render_template("paginas/premios.html", \
        titulo_pagina="Premios")
    
if __name__ == "__main__":
    app.run(debug=True)