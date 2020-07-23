
class Author:
    '''Author details'''
    def __init__(self, author_name, author_age, author_nationality):
        self.author_name = author_name
        self.author_age = author_age
        self.author_nationality = author_nationality

class Book:
    '''Book details'''
    def __init__(self, book_name, book_price, author_name, author_age, author_nationality):
        self.book_name = book_name
        self.book_price = book_price
        self.obj_author = Author(author_name, author_age, author_nationality)

def display_all_books(book_obj_list):
    print('        Available books \n')
    for book in book_obj_list:
        print('Book name: {}\nBook price: {}rupees\nAuthor name: {}\n_ _ _ _'.format(book.book_name, book.book_price, book.obj_author.author_name))

def affordable_books(book_obj_list):
    print('\n      Affordable books \n')
    for book in book_obj_list:
        if book.book_price < 1000:
            print('Book name: {}\nBook price: {}\n_ _ _ _'.format(book.book_name, book.book_price))

def books_written_by_particular_author(book_obj_list, name):
    try:
        count = 0
        for book in book_obj_list:
            if book.obj_author.author_name == name:
                count += 1
        if count >= 1:
            return '\n{} wrote {} book'.format(name, count)
        else:
            return '\nThere\'s no such book written by author {} in this book stall'.format(name)
    except Exception as e:
        print('Error. The exception was: {}', e)
        return 'Error'

book1 = Book('python', 999, 'guido van rossum', 64, 'dutch')
book2 = Book('scala', 1500, 'Martin Odersky', 61, 'german')
book3 = Book('java', 800, 'James Gosling', 65, 'canadian')
book4 = Book('C', 1999, 'dennis ritchie',79, 'american')
book5 = Book('C++', 1499, 'Bjarne Stroustrup', 69, 'danish')
book6 = Book('Generic Java', 599, 'Martin Odersky', 61, 'german')
book_obj_list = [book1, book2, book3, book4, book5, book6]

display_all_books(book_obj_list)
affordable_books(book_obj_list)
author_name_input= input('\nTo know how many books written by a particular author\nEnter the author name: ').strip().title()
no_of_books = books_written_by_particular_author(book_obj_list, author_name_input)
print(no_of_books)
