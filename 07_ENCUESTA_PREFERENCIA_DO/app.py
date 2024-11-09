from flask import Flask, render_template, request
from data_object import DataUser

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encuesta-preferencias", methods=['POST'])
def submit():
    if request.method=='POST':
        color=request.form['color']
        comida=request.form['comida']

        data_user=DataUser(color, comida)
        return render_template("resultados.html", user=data_user) 