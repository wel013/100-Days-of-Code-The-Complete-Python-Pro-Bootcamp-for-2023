from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
login_manager.init_app(app)
# if has this; when unautorized, will just go to login page
# login_manager.login_view = 'login'
# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    # def __init__(self, email: str, password: str, name: str):
    #     self.email = email
    #     self.password = password
    #     self.name = name
    #     self.is_authenticated = True
    #     self.is_active = True
    #     self.is_anonymous = True
    # @property
    # def is_authenticated(self):
    #     return True

    # @property
    # def is_active(self):
    #     return True

    # @property
    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return str(self.id)

    # def get_user(self, user_id):
    #     with app.app_context():
    #         user = db.get_or_404(User, user_id)
    #         return user


# @login_manager.user_loader
# def load_user(user_id):
#     with app.app_context():
#         user = db.get_or_404(User, user_id)
#         return user

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


with app.app_context():
    db.create_all()
    # db.session.query(User).delete()

    # # Commit the transaction
    # db.session.commit()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        secure_password = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=8)
        with app.app_context():
            user = db.session.execute(
                db.select(User).where(User.email == email)).scalar()
            if user:
                flash("That email already exit. Please try again.")
                return redirect(url_for("login"))
            new_user = User(
                name=name,
                email=email,
                password=secure_password
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            # flash('Logged in successfully.')
            return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        with app.app_context():
            user = db.session.execute(
                db.select(User).where(User.email == email)).scalar()
            if not user:
                flash("That email does not exit. Please try again.")

                return redirect(url_for("login"))

            elif not check_password_hash(user.password, password):
                flash("Incorrect password. Please try again.")

                return redirect(url_for("login"))
            if check_password_hash(user.password, password):

                login_user(user)

                # flash('Logged in successfully.')
                return redirect(url_for("secrets"))
                # return render_template("secrets.html", curr_user=user)
            else:
                flash('Invalid email or password', 'danger')
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    if not current_user.is_authenticated:
        return app.login_manager.unauthorized()
    return render_template("secrets.html", curr_user=current_user, logged_in=current_user.is_authenticated)
    # return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    # if not current_user.is_authenticated:
    #     return app.login_manager.unauthorized()
    file_path = app.static_folder + "/files"
    print(f"Serving file from: {file_path}")
    return send_from_directory(file_path,
                               "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
