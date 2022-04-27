from flask import Blueprint, render_template, request

import main.utils

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search')
def search_post():
    post_hash = request.args["post_hash"]
    posts = main.utils.search_post(post_hash)
    return render_template('post_list.html', posts=posts, post_hash=post_hash.lower().title())
