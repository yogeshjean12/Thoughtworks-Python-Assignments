from flask import Flask, request, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)


def connect_db():
    DATABASE_URL = "postgres+psycopg2://postgres:yogesh5201@localhost/flaskdemo"
    return create_engine(DATABASE_URL)


@app.route('/getbooks', methods=['GET'])
def get_all_books():
    res = view()
    result = [dict(row) for row in res]
    return jsonify(result)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['book_name']
        price = request.form['book_price']
        author_name = request.form['author_name']
        insert(name,price,author_name)
        return 'Book added successfully'


def view():
    books = db.execute('select * from book_stall.books')
    return books.fetchall()


def insert(name,price,author_name):
    db.execute(
        "INSERT INTO book_stall.books(book_name,book_price,author_name)"
        " VALUES('{}','{}','{}')"
        .format(name, price,author_name)
        )
    return

db = connect_db()


if __name__ == '__main__' :
    app.run(debug=True)
