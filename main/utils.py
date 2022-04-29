from json import JSONDecodeError, load

import logger


def load_all_post(url='posts.json'):
    """
    Загружает все посты из json файла
    """
    try:
        with open(url, 'r', encoding='UTF-8') as f:
            return load(f)
    # если нет файла с таким именем создаем новый файл
    except FileNotFoundError:
        f = open(url, 'x')
        f.close()
        return []
    # если не удалось преобразовать json файл сохраняем в лог информацию и возвращаем пустой список
    except JSONDecodeError:
        logger.main_logger.info("Не удалось преобразовать файл JSON")
        return []


def search_post(hashtag: str):
    """
    Возвращает все посты в которых есть подстрока введенная пользователем
    """
    all_posts = load_all_post()
    return list(filter(lambda x: hashtag.lower() in x['content'].lower(), all_posts))
