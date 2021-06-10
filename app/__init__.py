from flask import Flask, Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from environs import Env


# ----------------------------------------------
env = Env()
env.read_env()

# ----------------------------------------------
app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_SORT_KEYS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)

# ----------------------------------------------


class Blog(db.Model):
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)


db.create_all()

# ----------------------------------------------

bp = Blueprint("bp_blog", __name__, url_prefix="/api")


# ----------------------------------------------


@bp.get("/")
def home() -> str:
    blog = Blog()

    lista_de_posts: list = blog.query.all()
    for post in lista_de_posts:
        post.data = post.data.strftime("%d/%m/%Y")

    return render_template("/blog/home.html", posts=lista_de_posts)


@bp.route("/posts", methods=["GET", "POST"])
def get_register_posts() -> str:

    if request.method == "POST":
        print(request.form)
        db.session.add(Blog(**request.form))
        db.session.commit()
        return render_template("/blog/formulario.html")

    return render_template("/blog/formulario.html")


@bp.get("/posts/<int:post_id>")
def show_post(post_id: int) -> str:
    blog = Blog()

    post = blog.query.get(post_id)
    post.data = post.data.strftime("%d/%m/%Y")

    return render_template("/blog/post.html", post=post)


# ----------------------------------------------
app.register_blueprint(bp)
