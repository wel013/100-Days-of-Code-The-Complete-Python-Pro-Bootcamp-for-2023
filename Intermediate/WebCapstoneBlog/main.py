from flask import Flask, render_template
import requests
import datetime
app = Flask(__name__)


@app.route('/')
def home():
    url = "https://api.npoint.io/21eefacd756a601cb2f9"
    data = requests.get(url).json()
    author = "wenqian with npoint"
    current_time = datetime.datetime.now()
    time = f"{current_time.day} {current_time.month}, {current_time.year}"
    return render_template('index.html', all_blogs=data, author=author, date=time)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<id>')
def post(id):
    url = "https://api.npoint.io/21eefacd756a601cb2f9"
    data = requests.get(url).json()[int(id)-1]
    body = ""
    title = ""
    subtitle = ""
    # print(data)
    body = data["body"]
    title = data["title"]
    subtitle = data["subtitle"]
    return render_template("post.html", body=body, title=title, subtitle=subtitle)


if __name__ == "__main__":
    app.run(debug=True)
