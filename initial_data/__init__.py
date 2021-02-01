import csv, os

from bookstore_api import db
from books import Book
from customers import Customer

dir_path = os.path.dirname(os.path.realpath(__file__))
customers_csv = os.path.join(dir_path, 'tbl_customers.csv')
books_csv = os.path.join(dir_path, 'tbl_books.csv')


def _insert_books(books_csv=books_csv):
    with open(books_csv) as csv_file:
        spamreader = csv.reader(csv_file)
        for row in spamreader:
            book_obj = dict()
            book_obj['title'], book_obj['author'], book_obj['isbn'], book_obj['edition'], book_obj['year'], \
            book_obj['publishing_company'], book_obj['price'] = row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            book = Book(book_obj)
            if book.is_valid():
                db.session.add(book)


def _insert_customers(customers_csv=customers_csv):
    with open(customers_csv) as csv_file:
        spamreader = csv.reader(csv_file)
        for row in spamreader:
            customer_obj = dict()
            customer_obj['first_name'], customer_obj['last_name'], customer_obj['email'] = row[1], row[2], row[3]
            customer = Customer(customer_obj)
            if customer.is_valid():
                db.session.add(customer)


def insert():
    if not Customer.query.count() > 0 and not Book.query.count() > 0:
        print('[LOG] Inserindo Clientes.')
        _insert_customers()
        print('[LOG] Inserindo Livros.')
        _insert_books()
        db.session.commit()
    else:
        print(['[LOG] Base já preenchida.'])
