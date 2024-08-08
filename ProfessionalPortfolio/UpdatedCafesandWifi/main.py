from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class CafeandWifi(db.Model):
    __tablename__ = "cafes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(250), unique=False, nullable=False)
    loc_link: Mapped[str] = mapped_column(String(500), nullable=False)
    opentime: Mapped[str] = mapped_column(String(250), nullable=False)
    closetime: Mapped[str] = mapped_column(String(250), nullable=False)

    coffee: Mapped[str] = mapped_column(String(100), nullable=False)
    wifi: Mapped[str] = mapped_column(String(100), nullable=False)
    power: Mapped[str] = mapped_column(String(100), nullable=False)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')


with app.app_context():
    # db.drop_all()
    db.create_all()
    print("Created all")

coffee_choices = [
    ('❌', '❌'),
    ('☕', '☕'),
    ('☕☕', '☕☕'),
    ('☕☕☕', '☕☕☕'),
    ('☕☕☕☕', '☕☕☕☕'),
    ('☕☕☕☕☕', '☕☕☕☕☕')
]

wifi_choices = [
    ('❌', '❌'),
    ('📶', '📶'),
    ('📶📶', '📶📶'),
    ('📶📶📶', '📶📶📶'),
    ('📶📶📶📶', '📶📶📶📶'),
    ('📶📶📶📶📶', '📶📶📶📶📶')
]

power_choices = [
    ('❌', '❌'),
    ('⚡', '⚡'),
    ('⚡⚡', '⚡⚡'),
    ('⚡⚡⚡', '⚡⚡⚡'),
    ('⚡⚡⚡⚡', '⚡⚡⚡⚡'),
    ('⚡⚡⚡⚡⚡', '⚡⚡⚡⚡⚡')
]


class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    loc_link = StringField('Location', validators=[
                           DataRequired(), URL()])
    opentime = StringField('Open, eg 8:00AM', validators=[DataRequired()])
    closetime = StringField('Close, eg 10:00PM', validators=[DataRequired()])
    coffee = SelectField('Coffee', validators=[
                         DataRequired()], choices=coffee_choices)
    wifi = SelectField('Wifi', validators=[
                       DataRequired()], choices=wifi_choices)
    power = SelectField('Power', validators=[
                        DataRequired()], choices=power_choices)
    submit = SubmitField(label="submit")


class FilterEmojiForm(FlaskForm):
    coffee = SelectField('Filter Projects by Tag', choices=[
        ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
        validators=[DataRequired()])
    power = SelectField('Filter Projects by Tag', choices=[
        ('⚡', '⚡'), ('⚡⚡', '⚡⚡'), ('⚡⚡⚡', '⚡⚡⚡'), ('⚡⚡⚡⚡', '⚡⚡⚡⚡'), ('⚡⚡⚡⚡⚡', '⚡⚡⚡⚡⚡')],
        validators=[DataRequired()])
    wifi = SelectField('Filter Projects by Tag', choices=[
        ('📶', '📶'), ('📶📶', '📶📶'), ('📶📶📶', '📶📶📶'), ('📶📶📶📶', '📶📶📶📶'), ('📶📶📶📶📶', '📶📶📶📶📶')],
        validators=[DataRequired()])
    submit = SubmitField('Search')


\
@app.route("/", methods=['GET', 'POST'])
def home():
    form = FilterEmojiForm()
    if form.validate_on_submit() or request.method == "POST":
        coffee = form.coffee.data
        power = form.power.data
        wifi = form.wifi.data
        cafes = db.session.execute(
            db.select(CafeandWifi).where(CafeandWifi.coffee == coffee,
                                         CafeandWifi.power == power, CafeandWifi.wifi == wifi)
        ).scalars().all()
        return render_template('cafes.html', cafes=cafes)
    return render_template("index.html", form=form)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        name = form.name.data
        link = form.loc_link.data
        opent = form.opentime.data
        closet = form.closetime.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data
        print(name, link, opent, closet, coffee, wifi, power)
        with app.app_context():
            new_entry = CafeandWifi(
                name=name,
                loc_link=link,
                opentime=opent,
                closetime=closet,
                coffee=coffee,
                wifi=wifi,
                power=power
            )
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    cafes = db.session.execute(db.select(CafeandWifi)).scalars()
    return render_template('cafes.html', cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)
