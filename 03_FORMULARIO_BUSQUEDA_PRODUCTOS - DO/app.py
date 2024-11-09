from flask import Flask, render_template, request
from data_object import DataUser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/buscar-producto', methods=['GET'])
def submit():
    if request.method == 'GET':
        producto = request.args.get('producto')
        categoria = request.args.get('categoria')
        
        
        data_user=DataUser(producto, categoria)
        return render_template("resultados.html", user=data_user) 

if __name__ == "__main__":
    app.run(debug=True)


        