from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from bookstore_api.database import Base


class Customer(Base):
    __tablename__ = 'tbl_customers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(120), nullable=False, unique=True)

    _errors = []

    # creation_date = Column(DateTime, default=datetime.now(), nullable=False)
    # is_active = Column(Boolean, default=True, nullable=False)

    def __init__(self, data):
        self._errors = []
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']
        if 'email' in data:
            self.email = data['email']

    def update(self, data):
        self.__init__(data)

    def __repr__(self):
        return '<Customer {}>'.format(self.id)

    def as_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.columns}

    def is_valid(self):
        if not self.first_name:
            self._errors.append({'first_name': 'Este campo é obrigatório.'})
        if not self.last_name:
            self._errors.append({'last_name': 'Este campo é obrigatório.'})
        if not self.email:
            self._errors.append({'email': 'Este campo é obrigatório.'})
        if self.email and Customer.query.filter(Customer.email == self.email, Customer.id != self.id).first():
            self._errors.append({'email': 'O e-mail informado já encontra-se cadastrado.'})

        return True if not len(self._errors) else False

    def get_errors(self):
        return self._errors
