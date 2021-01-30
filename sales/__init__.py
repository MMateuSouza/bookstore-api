from flask import Blueprint, jsonify, request

from bookstore_api.database import db_session
from sales.models import Sale

sales = Blueprint('sales', __name__)


@sales.route('/', methods=['GET', 'POST'])
@sales.route('/<int:id>', methods=['GET'])
def index(id=None):
    if id:
        sale = Sale.query.get(id)
        if sale:
            return jsonify({'data': sale.as_dict()})
        return jsonify({'error': {'message': 'Id não encontrado.'}})

    elif request.method == 'GET':
        sales = Sale.query.all()
        return jsonify({'data': [sale.as_dict() for sale in sales]})

    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            sale = Sale(data)

            if sale.is_valid():
                sale.apply_discount()
                db_session.add(sale)
                db_session.commit()
                return jsonify({'data': sale.as_dict()})
            else:
                return jsonify({'errors': sale.get_errors()})

        return jsonify({'error': {'message': 'É esperado um objeto JSON.'}})
