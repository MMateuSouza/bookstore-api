from flask import Flask, jsonify, request
from dotenv import load_dotenv

from bookstore_api.database import db_session
from config import get_configuration_class

from books import books
from customers import customers
from sales import sales

load_dotenv()
configuration_object = get_configuration_class()

app = Flask(__name__)
app.config.from_object(configuration_object)

app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(customers, url_prefix='/customers')
app.register_blueprint(sales, url_prefix='/sales')


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'A URL `{}` nao e valida.'.format(request.path)}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': '[{}] metodo de requisicao invalido para a seguinte URL `{}`'.format(request.method,
                                                                                                  request.path)}), 405


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
