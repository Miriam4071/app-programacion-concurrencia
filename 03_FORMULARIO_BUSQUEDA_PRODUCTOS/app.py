from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/buscar-producto', methods=['GET'])
def submit():
    if request.method == 'GET':
        producto = request.args.get('producto')
        categoria = request.args.get('categoria')
        
        
        return f"categoria: {categoria}, producto: {producto}"

if __name__ == "__main__":
    app.run(debug=True)


        