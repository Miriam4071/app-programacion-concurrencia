from flask import Flask, render_template, request

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

        return f'Registro exitoso con el contacto {nombre}, {telefono}, con el siguente mensaje: {mensaje}'