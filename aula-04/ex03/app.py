from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'

links = [
    {"nome":"Francisco","url":"http://fra.com"},
     {"nome":"Joao","url":"http://joao.com"}
]
@app.route("/index")
def index():
    return render_template('index.html', 
links= links)
app.run(debug=True)
