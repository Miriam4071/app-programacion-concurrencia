from flask import Flask, render_template, request

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

        return f'Datos de la tarjeta de pago  Número de Tarjeta: {tarjeta}  Fecha de expiración: {expiracion} deactivate CVV: {cvv}'