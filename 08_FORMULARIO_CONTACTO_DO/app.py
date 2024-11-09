from flask import Flask, render_template, request
from data_object import DataUser

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar-contacto", methods=['POST'])
def submit():
    if request.method=='POST':
        nombre=request.form['nombre']
        telefono=request.form['telefono']
        mensaje=request.form['mensaje']

        data_user=DataUser(nombre, telefono, mensaje)
        return render_template("resultados.html", user=data_user) 