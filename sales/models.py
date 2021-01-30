from datetime import datetime
from sqlalchemy import Column, DateTime, Float, func, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config import Config

from bookstore_api.database import Base
from books.models import Book
from customers.models import Customer


class SaleBook(Base):
    __tablename__ = 'tbl_sales_books'
    id = Column(Integer, autoincrement=True, primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id))
    sale_id = Column(Integer, ForeignKey('tbl_sales.id'))
    book = relationship(Book, uselist=False)
    sale = relationship('Sale', uselist=False)
    quantity = Column(Integer, default=0, nullable=False)

    def __init__(self, book, quantity=0):
        self.book = book
        self.quantity = quantity

    def __repr__(self):
        return '<SaleBook {}>'.format(self.id)

    def as_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.columns}


class Sale(Base):
    __tablename__ = 'tbl_sales'
    id = Column(Integer, autoincrement=True, primary_key=True)
    customer_id = Column(Integer, ForeignKey(Customer.id), nullable=False)
    customer = relationship(Customer)
    subtotal = Column(Float, nullable=False, default=0)
    discount = Column(Float, nullable=False, default=0)
    grand_total = Column(Float, nullable=False, default=0)
    purchase_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    books = relationship('SaleBook')

    _tmp_list_of_books_ids = []
    _errors = []

    def __init__(self, data):
        if 'customer_id' in data:
            self.customer_id = data['customer_id']

        if 'books_ids' in data and type(data['books_ids']) == list and len(data['books_ids']) > 0:
            self._tmp_list_of_books_ids = data['books_ids']

        self.discount = self.subtotal = self.grand_total = 0

    def __repr__(self):
        return '<Sale {}>'.format(self.id)

    def as_dict(self):
        full_sale_dict = {field.name: getattr(self, field.name) for field in self.__table__.columns}
        full_sale_dict['shopping_cart'] = []
        for sale_book in self.books:
            sale_book_obj = sale_book.as_dict()
            sale_book_obj['book'] = sale_book.book.as_dict()
            full_sale_dict['shopping_cart'].append(sale_book_obj)
        return full_sale_dict

    def is_valid(self):
        if not self.customer_id:
            self._errors.append({'customer_id': 'Este campo é obrigatório.'})

        if not self._tmp_list_of_books_ids:
            self._errors.append({'books': 'Este campo é obrigatório e/ou é esperado uma lista de inteiros. Ela não pode estar vazia. Ex.: [1, 2, ..., 10]'})

        if self.customer_id and not Customer.query.get(self.customer_id):
            self._errors.append({'customer_id': 'Id não encontrado.'})

        if self._tmp_list_of_books_ids:
            error_obj = {'books_ids': []}
            ids_without_repetition = list(set(self._tmp_list_of_books_ids))
            for book_id in ids_without_repetition:
                book = Book.query.get(book_id)
                if book:
                    quantity = self._tmp_list_of_books_ids.count(book_id)
                    sale_book = SaleBook(book=book, quantity=quantity)
                    self.subtotal = self.subtotal + (book.price * quantity)
                    self.books.append(sale_book)
                else:
                    error_obj['books_ids'].append({'book_id': 'Id({}) não encontrado.'.format(book_id)})
            if len(error_obj['books_ids']) > 0:
                self._errors.append(error_obj)

        if self.books and len(self.books) > int(Config.MAX_BOOKS_PER_SALE):
            self._errors.append({'books_quantity': 'A quantidade máxima de livros distintos por compra foi atingido. O máximo é/são {}.'.format(Config.MAX_BOOKS_PER_SALE)})

        return True if not len(self._errors) else False

    def apply_discount(self):
        result = self.query.with_entities(
            func.sum(Sale.subtotal).label('amount_of_sales')
        ).filter(
            Sale.customer_id==self.customer_id
        ).first()

        amount_of_sales = result.amount_of_sales
        if amount_of_sales:
            if 1000 < amount_of_sales < 5000:
                self.discount = 0.1
            elif 5000 < amount_of_sales < 15000:
                self.discount = 0.15
            elif amount_of_sales > 15000:
                self.discount = 0.2

        self.grand_total = self.subtotal * (1 - self.discount)

    def get_errors(self):
        return self._errors
