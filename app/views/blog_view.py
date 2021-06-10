from flask import Blueprint, request, render_template
from http import HTTPStatus

from app import db
from app.models.blog_model import Blog

# ----------------------------------------------

bp = Blueprint("bp_blog", __name__, url_prefix="/api")


# ----------------------------------------------


@bp.get("/")
def home() -> str:

    lista_de_posts: list = Blog.query.all()

    for post in lista_de_posts:
        post.data = post.data.strftime("%d/%m/%Y")

    return render_template("/blog/home.html", posts=lista_de_posts), HTTPStatus.OK


@bp.route("/posts", methods=["GET", "POST"])
def get_register_posts() -> str:

    try:
        if request.method == "POST":
            db.session.add(Blog(**request.form))
            db.session.commit()

            return render_template("/blog/formulario.html"), HTTPStatus.OK

        return render_template("/blog/formulario.html"), HTTPStatus.OK

    except Exception as e:
        print(e)
        return render_template("not_found.html"), HTTPStatus.NOT_FOUND


@bp.get("/posts/<int:post_id>")
def show_post(post_id: int) -> str:

    try:
        post = Blog.query.get(post_id)
        post.data = post.data.strftime("%d/%m/%Y")

        return render_template("/blog/post.html", post=post), HTTPStatus.OK

    except Exception as e:
        print(e)
        return render_template("not_found.html"), HTTPStatus.NOT_FOUND


@bp.app_errorhandler(404)
def page_not_found(e) -> str:
    return render_template("not_found.html"), HTTPStatus.NOT_FOUND
