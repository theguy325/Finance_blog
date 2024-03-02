from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = response.json()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/post/<blog_id>")
def post(blog_id):
    return render_template("post.html", posts=blog_posts, id=int(blog_id))


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)