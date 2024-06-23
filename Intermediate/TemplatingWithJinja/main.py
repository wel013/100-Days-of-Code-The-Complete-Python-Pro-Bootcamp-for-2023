from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    data = requests.get(url).json()
    return render_template("index.html", all_posts=data)


@app.route('/post/<id>')
def post(id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
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
