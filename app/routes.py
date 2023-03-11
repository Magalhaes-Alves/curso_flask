#Rota é um endereço que será digitado no navegador que executará uma certa ação
#A função deve ter o mesmo nome da rota
#render_template irá montar o site com o arquivo html
from app import app
from flask import render_template
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    nome = "Gabriel"
    hora_atual = datetime.now().hour
    saudacao =''
    if hora_atual<6:
        saudacao= 'Boa Madrugada'
    elif hora_atual<12:
        saudacao = 'Bom dia'
    elif hora_atual <18:
        saudacao = 'Boa Tarde'
    else:
        saudacao = 'Boa noite'


    return render_template("index.html",nome=nome,saudacao =saudacao)
    
