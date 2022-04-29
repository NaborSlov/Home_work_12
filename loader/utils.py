import json

import logger
from main.utils import load_all_post


def save_file(file, content):
    """
    Сохранение картинки, если файл загружен возвращает True
    """
    filename = file.filename
    # проверка формата загружаемого файла
    if _is_filename_allowed(filename):
        # сохраняем файл
        file.save(f'./uploads/images/{filename}')
        # сохраняем новый пост в json
        _save_post_json(filename, content)
        return True

    logger.main_logger.info(f"Загруженный файл расширения({file.filename.split('.')[-1]}) не картинка")
    return False


def _save_post_json(filename, content):
    """
    Сохранение нового поста в json файле
    """
    # получение всех постов из json файла
    json_file = load_all_post()
    # информация для сохранения нового поста
    append_json = {'pic': f'/uploads/images/{filename}', 'content': content}
    json_file.append(append_json)

    with open("posts.json", 'w', encoding='UTF-8') as f:
        json.dump(json_file, f, indent=4, ensure_ascii=False)


def _is_filename_allowed(filename):
    """
    Проверка загружаемого файла на расширение "png", "jpeg", "jpg"
    """
    ALLOWED_EXTENSIONS = {"png", "jpeg", "jpg"}
    extension = filename.split('.')[-1]

    if extension in ALLOWED_EXTENSIONS:
        return True

    return False
