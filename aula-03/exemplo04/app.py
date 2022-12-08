from flask import Flask, render_template, redirect,request
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
def hello_world():
  return render_template('index.html',contatos=contatos)

#http://127.0.0.1:5000/salvar_contato/nator%2Fnator%40email.com%2F22222/familia%2Ctrabalho
@app.route('/salvar_contato',methods=['POST',])
def salvar_contato():
  #print((tags.split(',')))
  contatos.append(
    {
        "nome": request.form['nome'],
        "email": request.form['email'],
        "celular": request.form['celular'],
        "tags":request.form['tags'],
        'links_img_tag': ['familia']#[link_tags[i] for i in tags.split(',')]
    }
  )
  return redirect('/')
#http://127.0.0.1:5000/deletar_contato/nator%40email.com
@app.route('/deletar_contato',methods=['POST',])
def deletar_contato():
  for i in range(len(contatos)):
    #print(contatos[i])
    if contatos[i]['email'] == request.form['email']:
        contatos.pop(i)
        break
    print()
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
