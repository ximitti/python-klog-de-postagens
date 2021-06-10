from app import db


class Blog(db.Model):
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
