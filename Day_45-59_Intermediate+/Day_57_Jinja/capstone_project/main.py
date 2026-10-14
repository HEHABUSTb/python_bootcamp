import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    blog_posts = blog_response.json()

    return render_template("index.html", blog_posts=blog_posts)

@app.route('/post/<int:blog_id>')
def show_post(blog_id: int):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    blog_posts = blog_response.json()


    post = next(post for post in blog_posts if post.get('id') == int(blog_id))

    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
