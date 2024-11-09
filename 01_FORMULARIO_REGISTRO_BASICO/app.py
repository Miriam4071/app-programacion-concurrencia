from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    nombre=request.form['nombre']
    email=request.form['email']
    password=request.form['password']

    return f'Registro exitoso {nombre}, {email}, {password}'