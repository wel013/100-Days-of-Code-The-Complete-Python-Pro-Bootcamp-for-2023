from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)
# all_books = []


class books(db.Model):
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()
##############################################################################################


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(books).order_by(books.id))
        all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_name = request.form.get('book_name')
        book_author = request.form.get('book_author')
        rating = request.form.get('rating')
        with app.app_context():
            # db.create_all()
            entry = books(title=book_name,
                          author=book_author, rating=rating)
            db.session.add(entry)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    entry = db.session.execute(db.select(books).where(id == id)).scalar()
    name = entry.title
    author = entry.author
    id = entry.id
    curr_rating = entry.rating
    if request.method == 'POST':
        entry.rating = float(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", name=name, author=author, curr=curr_rating, id=id)


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    book_to_delete = db.get_or_404(books, id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
