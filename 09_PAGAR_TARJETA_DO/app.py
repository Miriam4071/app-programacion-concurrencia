from flask import Flask, render_template, request
from data_object import DataUser

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pagar", methods=['POST'])
def submit():
    if request.method=='POST':
        tarjeta=request.form['tarjeta']
        expiracion=request.form['expiracion']
        cvv=request.form['cvv']

        data_user=DataUser(tarjeta, expiracion, cvv)
        return render_template("resultado.html", user=data_user) 