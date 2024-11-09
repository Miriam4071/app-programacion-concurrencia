from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comentarios", methods=['POST'])
def submit():
    if request.method =='POST':
        nombre = request.form['nombre']
        email = request.form['email']
        comentario = request.form['comentario']

        return f'Registro exitoso el usuario es {nombre} con correo {email} y el comentario es {comentario} '