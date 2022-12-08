from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'

dados = [
    {"nome":"Francisco","idade":22},
     {"nome":"Joao","idade":13}
]
soma = 0
for i in dados:
    soma += int(i['idade'])
media = soma/len(dados)

@app.route("/index")
def index():
    return render_template(
            'index.html', 
            dados = dados,
            media = media#sum([int(i['idade']) for i in dados])/len(dados) 
    )
app.run(debug=True)
