from flask import Flask, render_template # Importando o render_template
# Criar a instância da aplicação Flask
app = Flask(__name__, template_folder='templates')


# Definir a rota principal da pagina inicial
@app.route('/')
def home():
    return render_template("home.html") # Certificando-se que o render_template será renderizado


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    return render_template("contato.html")


@app.route('/servicos', methods=['GET', 'POST'])
def servicos():
    return render_template('servicos.html')


@app.route('/sobre', methods=['GET', 'POST'])
def sobre():
    return render_template('sobre.html')


@app.route('/sintomas')
def sintomas():
    return render_template('sintomas.html')

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
