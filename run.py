from app import app,db

if __name__ == '__main__':
    with app.app_context():
       with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Erro ao criar o banco de dados: {e}")
    app.run(debug=True)