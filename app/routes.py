from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Produtos

@app.route('/') # Rota para a página inicial
def index():
    view_produtos = Produtos.query.all()
    return render_template('index.html', produtos=view_produtos)

@app.route('/cadastrar', methods=['GET', 'POST']) # Rota para a página de cadastro
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        descricao = request.form['descricao']
        estoque = request.form['estoque']
        imagem = request.form['imagem']
        novo_produto = Produtos(nome=nome, preco=preco, descricao=descricao, estoque=estoque, imagem=imagem)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST']) # Rota para a página de edição
def editar(id):
    produto = Produtos.query.get(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.preco = request.form['preco']
        produto.descricao = request.form['descricao']
        produto.estoque = request.form['estoque']
        produto.imagem = request.form['imagem']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', produto=produto)

@app.route('/deletar/<int:id>') # Rota para deletar um produto
def deletar(id):
    produto = Produtos.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('index'))
