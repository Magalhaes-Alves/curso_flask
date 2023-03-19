#Rota é um endereço que será digitado no navegador que executará uma certa ação
#A função deve ter o mesmo nome da rota
#render_template irá montar o site com o arquivo html
from app import app
from flask import render_template
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    hora_atual = datetime.now().hour
    saudacao =''
    dados = {
        'nome': 'gabriel',
        'profissao': 'programador',
        'idade': '21'
        }
    jogos_favoritos = ['The Legend Of Zelda: Ocarina of Time','Xcom', 'Metal Gear Solid V: The Phantom Pain']
    if hora_atual<6:
        saudacao= 'Boa Madrugada'
    elif hora_atual<12:
        saudacao = 'Bom dia'
    elif hora_atual <18:
        saudacao = 'Boa Tarde'
    else:
        saudacao = 'Boa noite'


    return render_template("index.html",dados=dados,saudacao =saudacao,jogos =jogos_favoritos)
    

@app.route('/contato')
def contato():
    dados = {
        'nome': 'gabriel',
        'profissao': 'programador',
        'idade': '21'
    }
    jogos_favoritos = ['The Legend Of Zelda: Ocarina of Time','Xcom', 'Metal Gear Solid V: The Phantom Pain']

    return render_template('contato.html',dados=dados,jogos=jogos_favoritos)