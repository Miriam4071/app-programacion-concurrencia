from flask import Flask, render_template, request
from data_object import DataUser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inscripcion-evento", methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        asistencia = request.form['asistencia']

        data_user=DataUser(nombre, email, asistencia)
        return render_template("resultados.html", user=data_user) 
