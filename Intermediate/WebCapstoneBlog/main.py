from flask import Flask, render_template, request
# import request
import requests
import datetime
import csv
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    message = request.form['message']
    print(name, phone, email, message)
    try:
        with open("/home/liwq/Desktop/Python_Bootcamp/day_60_api_forms/contact.csv", "w", newline='') as f:
            writer = csv.writer(f)
            # Write header
            # writer.writerow(["Name", "Phone", "Email", "Message"])
            writer.writerow([name, phone, email, message])  # Write data
        print("File created and data written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return render_template("contact.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
