from flask import Flask, render_template,request
from data_object import DataUser

app=Flask(__name__)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/reservar-hotel", methods=['POST'])
def submit():
    if request.method =='POST':
        fechaEntrada=request.form['checkin']
        fechaSalida=request.form['checkout']
        personas=request.form['personas']

        data_user=DataUser(fechaEntrada, fechaSalida, personas)
        return render_template("resultados.html", user=data_user) 