from sqlalchemy import Column, Integer, String, Float, SmallInteger

from bookstore_api import db
from books.validators import validate_isbn


class Book(db.Model):
    __tablename__ = 'tbl_books'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(120), nullable=False)
    author = Column(String(120), nullable=False)
    isbn = Column(String(13), nullable=False,
                  unique=True)  # Valor obtido por meio do seguinte link https://servicos.cbl.org.br/isbn/manual/manual-do-ISBN.pdf
    edition = Column(SmallInteger, nullable=False)
    year = Column(String(4), nullable=False)
    publishing_company = Column(String(120), nullable=False)
    price = Column(Float, nullable=False)

    _errors = []

    def __init__(self, data):
        self._errors = []
        self._isbn = self.isbn
        if 'title' in data:
            self.title = data['title']
        if 'author' in data:
            self.author = data['author']
        if 'isbn' in data:
            self._isbn = data['isbn']
        if 'edition' in data:
            self.edition = data['edition']
        if 'year' in data:
            self.year = data['year']
        if 'publishing_company' in data:
            self.publishing_company = data['publishing_company']
        if 'price' in data:
            self.price = data['price']

    def update(self, data):
        self.__init__(data)

    def __repr__(self):
        return '<Book {}>'.format(self.id)

    def as_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.columns}

    def is_valid(self):
        if not self.title:
            self._errors.append({'title': 'Este campo é obrigatório'})
        if not self.author:
            self._errors.append({'author': 'Este campo é obrigatório'})
        if not self._isbn:
            self._errors.append({'isbn': 'Este campo é obrigatório'})
        if not self.edition:
            self._errors.append({'edition': 'Este campo é obrigatório'})
        if not self.year:
            self._errors.append({'year': 'Este campo é obrigatório'})
        if not self.publishing_company:
            self._errors.append({'publishing_company': 'Este campo é obrigatório'})
        if not self.price:
            self._errors.append({'price': 'Este campo é obrigatório'})
        if self._isbn:
            if validate_isbn(self._isbn):
                if Book.query.filter(Book.isbn == self._isbn, Book.id != self.id).first():
                    self._errors.append({'isbn': 'O isbn informado já encontra-se cadastrado.'})
                else:
                    self.isbn = self._isbn
            else:
                self._errors.append({'isbn': 'O isbn informado é inválido.'})

        return True if not len(self._errors) else False

    def get_errors(self):
        return self._errors
