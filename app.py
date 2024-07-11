
from flask import Flask
from blueprints.books_blueprint import books_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)

if __name__ == '__main__':
    app.run()
