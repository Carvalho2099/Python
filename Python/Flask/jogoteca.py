from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import JogoDao, UsuarioDao
import pymysql
from models import Jogo, Usuario


app = Flask(__name__)
app.secret_key = 'NadaAqui'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1945"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

db = pymysql.connect(host='localhost', user='root', db='jogoteca', password='1945')

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template(
        'lista.html',
        titulo='Jogos',
        jogos=lista
    )


@app.route('/novo')
def novo():
    if 'usuário_logado' not in session or session['usuário_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template(
        'novo.html',
        titulo='Novo Jogo'
    )


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuário_logado'] = usuario.id
            flash(f"{usuario.nome} logou com sucesso!")
            proxima_pagina = request.form['proxima']
            return redirect(url_for(proxima_pagina))
    flash('Não logado. Tente novamente...')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuário_logado'] = None
    flash('Nenhum usuário logado.')
    return redirect(url_for('index'))


app.run(debug=True)
