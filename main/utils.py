import json


def load_all_post(url='posts.json'):
    try:
        with open(url, 'r', encoding='UTF-8') as f:
            return json.load(f)
    except FileNotFoundError:
        f = open(url, 'x')
        f.close()
        return []


def search_post(hashtag: str):
    all_posts = load_all_post()
    return list(filter(lambda x: hashtag.lower() in x['content'].lower(), all_posts))


