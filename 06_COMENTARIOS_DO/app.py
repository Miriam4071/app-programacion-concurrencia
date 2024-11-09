from flask import Flask, render_template,request
from data_object import DataUser

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

        data_user=DataUser(nombre, email, comentario)
        return render_template("resultados.html", user=data_user) 