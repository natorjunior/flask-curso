from flask import Flask, render_template,redirect,request
app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
link_tags = {
    "trabalho":'https://cdn-icons-png.flaticon.com/512/2452/2452717.png',
    "familia":'https://cdn-icons-png.flaticon.com/512/2452/2452717.png',
    "estudo":'https://cdn-icons-png.flaticon.com/512/2452/2452717.png',
}
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
  return render_template('index.html',contatos=contatos,link_tags=link_tags, zip=zip)
@app.route("/salvar_contato", methods=['POST'])
def salvar_contato():
    contatos.append({
        "nome": request.form['nome'],
        "email": request.form['email'],
        "celular": request.form['celular'],
        "tags":request.form['tags'],
        'links_img_tag': ['familia']
    })
    return redirect('/')

@app.route("/deletar_contato", methods=['POST'])
def deletar_contato():
    print(request.form['email'])
    for i in range(len(contatos)):
        if contatos[i]['email'] == request.form['email']: #Verifica o email recebido
            contatos.pop(i)
            break            
    return redirect('/')

@app.route("/editar_contato", methods=['POST'])
def editar_contato():
    print(request.form)
    for i in range(len(contatos)):
        if contatos[i]['email'] == request.form['email']: #Verifica o email recebido
            contatos[i]['nome'] = request.form['nome']
            contatos[i]['email'] = request.form['email']
            contatos[i]['celular'] = request.form['celular']
            break            
    return redirect('/')
app.run(debug=True)
