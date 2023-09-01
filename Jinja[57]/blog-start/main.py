from flask import Flask, render_template
import requests
from post import Post

post_obj = Post()
blog_data = post_obj.blog_data
# print(blog_data)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_data=blog_data)


@app.route('/<int:post_index>')
def get_blog_post(post_index):
    try:
        post_data = blog_data[post_index - 1]
    except IndexError:
        return "<h1>Error 404!</h1>" \
               "<p>This page does not exists.</p>"
    title = post_data['title']
    subtitle = post_data['subtitle']
    body = post_data['body']
    return render_template("post.html", post_title=title, post_subtitle=subtitle, post_body=body)


if __name__ == "__main__":
    app.run(debug=True)
