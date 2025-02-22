from app import db

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(80), unique=True)
    preco = db.Column(db.Float)
    descricao = db.Column(db.String(255))
    estoque = db.Column(db.Integer)
    imagem = db.Column(db.String(255))