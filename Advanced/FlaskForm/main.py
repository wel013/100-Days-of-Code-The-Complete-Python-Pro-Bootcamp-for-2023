from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap4
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
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


app.secret_key = "/"


class MyForm(FlaskForm):
    # for clarity specify the lable property
    # this is what gets passed into the login.html
    email = StringField(label='email', validators=[
                        DataRequired(), validators.Email()])
    password = PasswordField(label='password',  validators=[
                             DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    email = "admin@email.com"
    password = "12345678"
    if form.validate_on_submit():
        # if request.method == 'POST' and form.validate():
        if form.email.data == email and form.password.data == password:
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)


@app.route('/success')
def success():
    return render_template("success.html")


@app.route('/denied')
def denied():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
