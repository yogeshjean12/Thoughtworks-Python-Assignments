from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine

app = Flask(__name__)

DATABASE_URL = "postgres+psycopg2://postgres:yogesh5201@localhost/flaskdemo"
db = create_engine(DATABASE_URL)


class Book():
    id = Column(Integer, primary_key=True)
    book_name = Column(String(20), unique=True, nullable=True)
    book_price = Column(Integer, unique=False, nullable=True)
    author_name = Column(String(20), unique=False, nullable=True)

    def __init__(self, book_name, book_price, author_name):
        self.book_name = book_name
        self.book_price = book_price
        self.author_name = author_name


@app.route('/getbooks', methods=['GET'])
def get_all_books():
    books = db.execute('select * from book_stall.books')
    result = [dict(row) for row in books]
    return jsonify(result)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['book_name']
        price = request.form['book_price']
        author_name = request.form['author_name']
        db.execute("INSERT INTO book_stall.books(book_name,book_price,author_name) VALUES('{}','{}','{}')".format(name, price, author_name))
        return 'Book added successfully'


if __name__ == '__main__' :
    app.run(debug=True)
