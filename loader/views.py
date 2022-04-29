from flask import Blueprint, render_template, request

import logger
import loader.utils


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def get_form_post():
    """
    Вьюшка с формой добавления нового поста, GET-method
    """
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["POST"])
def save_post():
    """
    Вьюшка для обработки post запроса нового поста
    """
    # получение картинки из формы
    file = request.files['picture']
    # получение текста поста
    content = request.form.get('content')
    # сохранение и проверка на то что файл загружен
    if loader.utils.save_file(file, content):
        # получение пути до новой картинки
        picture = f"/uploads/images/{file.filename}"
        return render_template("post_uploaded.html", picture=picture, content=content)
    else:
        logger.main_logger.error("Ошибка загрузки файла")
        return '<h1>Ошибка загрузки</h1>'
