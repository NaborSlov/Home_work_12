from flask import Flask

from main.views import main_blueprint
from loader.views import loader_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


if __name__ == '__main__':
    app.run(debug=True)


