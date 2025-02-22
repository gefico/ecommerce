from flask import render_template, request, redirect, url_for,session
from app import app, db
from app.models import Produtos,User
from werkzeug.security import generate_password_hash, check_password_hash

def admin_required():
    loggedin = session.get('loggedin')
    is_admin = False  # Inicialize is_admin como False por padrão

    if loggedin:
        user = User.query.get(session['id'])
        if user:
            is_admin = user.is_admin

    print(f"loggedin: {loggedin}, is_admin: {is_admin}")

    if not loggedin or not is_admin:
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['loggedin'] = True
            session['id'] = user.id
            session['username'] = user.username
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error='Usuário ou senha incorretos')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/') # Rota para a página inicial
def index():
    view_produtos = Produtos.query.all()
    return render_template('produtos.html', produtos=view_produtos)

@app.route('/produto/<int:id>') # Rota para a página de detalhes do produto
def produto(id):
    produto = Produtos.query.get(id)
    return render_template('detalhe_produto.html', produto=produto)

@app.route('/admin') # Rota para a página sobre
def admin():
    admin_required()
    view_produtos = Produtos.query.all()
    return render_template('index.html', produtos=view_produtos)

@app.route('/cadastrar', methods=['GET', 'POST']) # Rota para a página de cadastro
def cadastrar():
    admin_required()
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        descricao = request.form['descricao']
        estoque = request.form['estoque']
        imagem = request.form['imagem']
        novo_produto = Produtos(nome=nome, preco=preco, descricao=descricao, estoque=estoque, imagem=imagem)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('cadastrar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST']) # Rota para a página de edição
def editar(id):
    admin_required()
    produto = Produtos.query.get(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.preco = request.form['preco']
        produto.descricao = request.form['descricao']
        produto.estoque = request.form['estoque']
        produto.imagem = request.form['imagem']
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('editar.html', produto=produto)

@app.route('/deletar/<int:id>') # Rota para deletar um produto
def deletar(id):
    admin_required()
    produto = Produtos.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('admin'))
