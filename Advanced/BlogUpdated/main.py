from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '<insert your key>'
Bootstrap5(app)
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def get_all_posts():
    posts = []
    with app.app_context():
        posts = db.session.execute(
            db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    return render_template("index.html", all_posts=posts)




# @app.route('/post/<int:post_id>')
# def retrieve_single_post(post_id):
#     with app.app_context():
#         post = db.session.execute(db.select(BlogPost).where(BlogPost.id=post_id)).scalar()
#         return render_template("post.html", post=post)


# @app.route('/')
@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    with app.app_context():
        post = db.session.execute(db.select(BlogPost).where(
            BlogPost.id == post_id)).scalar()
        return render_template("post.html", post=post)




@app.route('/new-post', methods=["POST", "GET"])
def new_post():
    add_form = PostForm()
    if add_form.validate_on_submit():
        new_post = BlogPost(
            title=add_form.title.data,
            subtitle=add_form.subtitle.data,
            author=add_form.author.data,
            date=date.today().strftime('%B %d, %Y'),
            body=add_form.body.data,
            img_url=add_form.img_url.data
        )
        with app.app_context():
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
    return render_template('make-post.html', form=add_form)



@app.route('/edit-post/<int:post_id>', methods=['GET', "POST"])
def edit_post(post_id):
    with app.app_context():
        post = db.get_or_404(BlogPost, post_id)
        # pre-populate so that user does not have to retype
        edit_form = PostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        if edit_form.validate_on_submit():
            title = edit_form.title.data
            subtitle = edit_form.subtitle.data
            author = edit_form.author.data
            # date = edit_form.date.data,
            body = edit_form.body.data
            img_url = edit_form.img_url.data
            post.title = title
            post.subtitle = subtitle
            post.author = author
            # post.date = date
            post.body = body
            post.img_url = img_url
            db.session.commit()
            return redirect(url_for("show_post", post_id=post_id))

    return render_template('make-post.html', form=edit_form, post_id=post_id)


@app.route('/delete_post/<int:post_id>', methods=['GET', "POST"])
def delete_post(post_id):
    with app.app_context():
        post_to_delete = db.get_or_404(BlogPost, post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
