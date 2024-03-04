from flask import Flask, render_template, request
import requests
import smtplib
import os

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


@app.route("/contact", methods=["POST", 'GET'])
def contact():
    if request.method == 'POST':
        my_email = "sendernishant@gmail.com"
        my_password = "Your Password"
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']
        mail_body = f"Name:{name}\nMobile:{phone}\nEmail:{email}\nMessage:{message}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(to_addrs='5511nishant@gmail.com', from_addr=my_email,
                                msg=f"Subject: Message from a follower!!\n\n{mail_body}")

        return render_template('contact.html', message="post")
    else:
        return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)