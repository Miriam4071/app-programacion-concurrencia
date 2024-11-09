from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encuesta-preferencias", methods=['POST'])
def submit():
    if request.method=='POST':
        color=request.form['color']
        comida=request.form['comida']

        return f'Registro exitoso {color} y {comida} son de su preferencia'