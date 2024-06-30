from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
# Define choices with emojis
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


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


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
        with open('cafe-data.csv', 'a',  newline='') as csv_file:
            employee_writer = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(
                [name, link, opent, closet, coffee, wifi, power])

            # Exercise:
            # Make the form write a new row into cafe-data.csv
            # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
