from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<h1>Lais testando... Aula foi boa!<h1/>"

if __name__ == '__main__':
    app.run()