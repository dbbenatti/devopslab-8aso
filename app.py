from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "<h1>Laboratório DevOps - FIAP 8ASO</h1>"

if __name__ == '__main__':
    app.run()