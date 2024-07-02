# created using The Movie Database: https://www.themoviedb.org/
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, asc, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mymovies.db"
app.config['SECRET_KEY'] = '<fill in secret key>'
Bootstrap5(app)

# CREATE DB


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)
# CREATE TABLE


class movies(db.Model):
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(
        String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer,  nullable=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250),  nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)


#
#################################################################################################################################################################################################################################################
# adding a movie:
new_movie = movies(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
second_movie = movies(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)
# with app.app_context():
# db.create_all()
# db.session.add(new_movie)

# db.session.add(second_movie)
# db.session.commit()
#######################################################################################################


class MyForm(FlaskForm):
    # for clarity specify the lable property
    # this is what gets passed into the login.html
    rating = DecimalField(label='Rating', validators=[
        DataRequired()])
    review = StringField(label='review',  validators=[
        DataRequired()])
    submit = SubmitField(label="Edit")


class AddForm(FlaskForm):
    # for clarity specify the lable property
    # this is what gets passed into the login.html
    name = StringField(label='Name',  validators=[
        DataRequired()])
    submit = SubmitField(label="Add")


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(
            db.select(movies).order_by(desc(movies.rating)))
        all_movies = result.scalars().all()
        # res = result.all()
        # print(res)
        for index, movie in enumerate(all_movies):
            movie.ranking = index + 1
        # db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    form = MyForm()
    movie_title = ''
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        # print(rating)
        # print(review)
        # print(id)
        with app.app_context():
            res = db.session.execute(
                db.select(movies).where(movies.id == id)).scalar()
            movie_title = res.title
            res.rating = rating
            res.review = review
            # print(res.title)
            # print(res.rating, res.review)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=form, name=movie_title)


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    with app.app_context():
        res = db.session.execute(
            db.select(movies).where(movies.id == id)).scalar()
        db.session.delete(res)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.name.data
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=true&language=en-US&page=1"
           headers = {
            "accept": "application/json",
            "Authorization": "<fill in your bear auth>"
        }
        response = requests.get(url, headers=headers).json()
        return render_template('select.html', list_of_movies=response['results'])

    return render_template('add.html', form=form)
# cannot combine with add


@app.route('/find', methods=["GET", "POST"])
def find():
    if request.method == 'GET':
        movie_id = request.args.get('id')
        print(movie_id)
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "<fill in your bear auth>"
        }

        response1 = requests.get(url, headers=headers).json()
        print(response1)
        description = response1["overview"]
        poster = response1['poster_path']
        img_url = f"https://image.tmdb.org/t/p/original{poster}"
        year = response1['release_date']
        year = year.split('-')[0]
        title = response1["title"]
        with app.app_context():
            new_movie = movies(title=title, year=year,
                               description=description, img_url=img_url)
            db.session.add(new_movie)
            db.session.commit()
            res = db.session.execute(
                db.select(movies).where(movies.title == title)).scalar()
            edit_id = res.id
            return redirect(url_for('edit', id=edit_id))


if __name__ == '__main__':
    app.run(debug=True)
