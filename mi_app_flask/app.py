from flask import Flask, render_template, request

@app.route('/sumit', methods=['POST'])
def submit():
    if request.method=='POST':
        nombre=request.form['nombre']
        email=request.form['email']
        password=request.form['password']

        return f'Registro exitoso para {nombre} con el correo {email}'
