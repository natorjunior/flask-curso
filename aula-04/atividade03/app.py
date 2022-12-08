from flask import Flask, render_template
app = Flask(__name__)
class Car:
    def __init__(self,nome,marca,modelo,cor) -> None:
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
obj1 = Car('car1','fiat','Fiat uno','red')
obj2 = Car('car2','fiat','Fiat toro','blue')
obj3 = Car('car3','fiat','Fiat uno','black')
dados = [obj1,obj2,obj3]

@app.route("/index")
def index():
    return render_template(
            'index.html', 
            dados = dados
    )
app.run(debug=True)

#jinja2 snippet kit 
#https://github.com/natorjunior/flask-curso