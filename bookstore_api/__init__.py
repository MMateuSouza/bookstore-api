from flask import Flask
from dotenv import load_dotenv

from bookstore_api.database import db_session
from config import get_configuration_class

from books import books
from customers import customers

load_dotenv()
configuration_object = get_configuration_class()

app = Flask(__name__)
app.config.from_object(configuration_object)

app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(customers, url_prefix='/customers')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
