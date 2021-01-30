from setuptools import setup

setup(
    name='bookstore_api',
    packages=['bookstore_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'psycopg2',
        'python-dotenv'
    ],
)