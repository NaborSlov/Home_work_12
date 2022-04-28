from flask import Blueprint, render_template, request


import loader.utils


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def get_form_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["POST"])
def save_post():
    file = request.files.get('picture')
    content = request.form.get('content')
    if loader.utils.save_file(file, content):
        picture = f"/uploads/images/{file.filename}"
        return render_template("post_uploaded.html", picture=picture, content=content)
    else:
        return '<h1>Ошибка загрузки"</h1>'


