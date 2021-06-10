from flask import Flask


def init_app(app: Flask) -> None:
    from .blog_view import bp as bp_blog

    app.register_blueprint(bp_blog)
