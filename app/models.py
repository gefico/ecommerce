from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Novo campo

    def __repr__(self):
        return '<User %r>' % self.username


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(80), unique=True)
    preco = db.Column(db.Float)
    descricao = db.Column(db.String(255))
    estoque = db.Column(db.Integer)
    imagem = db.Column(db.String(255))