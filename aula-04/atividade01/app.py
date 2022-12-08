from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'

dados = [
    {"nome":"Francisco","idade":22},
     {"nome":"Joao","idade":13}
]
@app.route("/index")
def index():
    return render_template('index.html', 
dados= dados)
app.run(debug=True)
