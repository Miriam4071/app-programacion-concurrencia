from flask import Flask, render_template,request
from data_object import DataUser

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit-survey', methods=['POST'])

def submit():
    if request.method =='POST':
        nombre=request.form['nombre']
        satisfaccion=request.form['satisfaccion']
        comentarios=request.form['comentarios']

        data_user=DataUser(nombre, satisfaccion, comentarios)
        return render_template("resultado.html", user=data_user) 