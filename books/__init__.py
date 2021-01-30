from flask import Blueprint, jsonify, request

from bookstore_api import db_session
from books.models import Book

books = Blueprint('books', __name__)


@books.route('/', methods=['GET', 'POST'])
@books.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def books_view(id=None):
    if not id:

        if request.method == 'GET':
            books = Book.query.all()
            return jsonify({'data': [book.as_dict() for book in books]})

        elif request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                book = Book(data)

                if book.is_valid():
                    db_session.add(book)
                    db_session.commit()
                    return jsonify({'data': book.as_dict()})
                else:
                    return jsonify({'errors': book.get_errors()})

            return jsonify({'error': {'message': 'É esperado um objeto JSON.'}})

    book = Book.query.get(id)

    if book:
        if request.method == 'GET':
            return jsonify({'data': book.as_dict()})

        elif request.method == 'PUT':
            if request.is_json:
                data = request.get_json()
                book.update(data)

                if book.is_valid():
                    db_session.commit()
                    return jsonify({'data': book.as_dict()})
                else:
                    return jsonify({'errors': book.get_errors()})

            return jsonify({'error': {'message': 'É esperado um objeto JSON.'}})

        elif request.method == 'DELETE':
            db_session.delete(book)
            db_session.commit()
            return jsonify({'data': {}})

    return jsonify({'error': {'message': 'Id não encontrado.'}})
