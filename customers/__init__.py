from flask import Blueprint, jsonify, request

from bookstore_api import db_session
from customers.models import Customer

customers = Blueprint('customers', __name__)


@customers.route('/', methods=['GET', 'POST'])
@customers.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def customers_view(id=None):
    if not id:

        if request.method == 'GET':
            customers = Customer.query.all()
            return jsonify({'data': [customer.as_dict() for customer in customers]})

        elif request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                customer = Customer(data)

                if customer.is_valid():
                    db_session.add(customer)
                    db_session.commit()
                    return jsonify({'data': customer.as_dict()})
                else:
                    return jsonify({'errors': customer.get_errors()})

            return jsonify({'error': {'message': 'É esperado um objeto JSON.'}})

    customer = Customer.query.get(id)

    if customer:
        if request.method == 'GET':
            return jsonify({'data': customer.as_dict()})

        elif request.method == 'PUT':
            if request.is_json:
                data = request.get_json()
                customer.update(data)

                if customer.is_valid():
                    db_session.commit()
                    return jsonify({'data': customer.as_dict()})
                else:
                    return jsonify({'errors': customer.get_errors()})

            return jsonify({'error': {'message': 'É esperado um objeto JSON.'}})

        elif request.method == 'DELETE':
            db_session.delete(customer)  # Verificar futuramente a possibilidade de aplicar-se a deleção lógica.
            db_session.commit()
            return jsonify({'data': {}})

    return jsonify({'error': {'message': 'Id não encontrado.'}})
