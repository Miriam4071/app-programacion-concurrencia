from flask import Flask, render_template,request

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

        return f'Registro exitoso, la reserva del hotel es {fechaEntrada} hasta {fechaSalida} y con {personas} personas'