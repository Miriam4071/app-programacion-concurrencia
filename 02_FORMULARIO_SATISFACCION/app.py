from flask import Flask, render_template,request

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

        return f'Registro exitoso para {nombre} con su nivel de {satisfaccion} y su {comentarios}'