import json

from main.utils import load_all_post


def save_file(file, content):
    ALLOWED_EXTENSIONS = {"png", "jpeg", 'jpg'}
    filename = file.filename
    extension = filename.split('.')[-1]
    if extension in ALLOWED_EXTENSIONS:
        file.save(f'./uploads/images/{file.filename}')
        _save_post_json(filename, content)
        return True
    else:
        return False


def _save_post_json(filename, content):
    json_file = load_all_post()
    append_json = {'pic': f'/uploads/images/{filename}', 'content': content}
    json_file.append(append_json)
    with open("posts.json", 'w', encoding='UTF-8') as f:
        json.dump(json_file, f, indent=4, ensure_ascii=False)
