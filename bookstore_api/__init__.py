from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
CORS(app)
FLASK_ENV = getenv('FLASK_ENV')
if FLASK_ENV == 'development':
    app.config.from_object('config.DevelopmentConfig')
elif FLASK_ENV == 'production':
    app.config.from_object('config.ProductionConfig')
if FLASK_ENV == 'testing':
    app.config.from_object('config.TestingConfig')
db = SQLAlchemy(app)

from books import books
from customers import customers
from sales import sales

app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(customers, url_prefix='/customers')
app.register_blueprint(sales, url_prefix='/sales')

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': {
        'message': str(error),
        'url': request.path,
    }}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'A URL `{}` nao e valida.'.format(request.path)}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': '[{}] metodo de requisicao invalido para a seguinte URL `{}`'.format(request.method,
                                                                                                  request.path)}), 405

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
