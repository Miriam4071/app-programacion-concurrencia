from flask import Flask

app=Flask(__name__)

@app.route("/pagina_1")
def pagina_1():
    return "<h1>Página 1</h1>"

@app.route("/pagina_2")
def pagina_2():
    return "<h1>Página 2</h1>"