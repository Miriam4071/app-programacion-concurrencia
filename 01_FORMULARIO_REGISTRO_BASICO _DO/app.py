from flask import Flask, render_template,request
from data_object import DataUser  


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    nombre=request.form['nombre']
    email=request.form['email']
    password=request.form['password']

    data_user=DataUser(nombre, email, password)
    return render_template("resultado.html", user=data_user)

    