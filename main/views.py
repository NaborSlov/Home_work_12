from flask import Blueprint, render_template, request, send_from_directory
import logger

import main.utils


main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    Фьюшка для вывода главной формы
    """
    return render_template("index.html")


@main_blueprint.route('/search')
def search_post():
    """
    Фьюшка для поиска постов
    """
    # получение данных пользователя из адресной строки
    post_hash = request.args["post_hash"].lower().title()
    # получение всех постов по данным пользователя
    posts = main.utils.search_post(post_hash)
    logger.main_logger.info(f"Выполнен поиск по значению {post_hash}")
    return render_template('post_list.html', posts=posts, post_hash=post_hash)


@main_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    """
    Фьюшка для доступа к файлам из папки uploads
    """
    return send_from_directory("uploads", path)
