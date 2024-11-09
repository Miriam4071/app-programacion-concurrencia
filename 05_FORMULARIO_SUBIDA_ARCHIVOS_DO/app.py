from flask import Flask,render_template,request
from data_object import DataUser
import os

app=Flask(__name__)

FOLDER = 'uploads'
app.config['FOLDER'] = FOLDER



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def submit():
    if request.method=='POST':
       
         if 'archivo' not in request.files or request.files['archivo'].filename == '':
             return 'No se subió ningún archivo :('
    
    archivo = request.files['archivo']

    archivo.save(os.path.join(app.config['FOLDER'], archivo.filename))

    data_user=DataUser(archivo)
    return render_template("resultados.html", user=data_user) 

