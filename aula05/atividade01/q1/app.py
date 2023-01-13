from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
link_tags = {"trabalho":'https://cdn-icons-png.flaticon.com/512/2452/2452717.png',"familia":'https://cdn-icons-png.flaticon.com/512/2452/2452717.png'}
contatos = [{
        "nome":"fulano",
        "email":"fulano@email.com",
        "celular":"00000000",
        "tags":["trabalho"],
        'links_img_tag':[
            'https://cdn-icons-png.flaticon.com/512/2452/2452717.png',
        ]
    },{
        "nome":"joao",
        "email":"joao@email.com",
        "celular":"111111111",
        "tags":["familia"],
        'links_img_tag':[
            'https://cdn-icons-png.flaticon.com/512/2452/2452717.png',
            #"https://cdn-icons-png.flaticon.com/512/1374/1374128.png"
        ]
    }]


@app.route('/')
def index():
  return render_template('index.html',contatos=contatos,link_tags=link_tags)
app.run(debug=True)
