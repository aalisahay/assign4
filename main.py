from flask import render_template
from create_db import app, db, Book, create_books

@app.route('/')
def index():
	return render_template('hello.html')
	
@app.route('/books/')
def book():
	books = db.session.query(Book).all()
	return render_template('books.html', books = books)
	
if __name__ == "__main__":
	app.run()
