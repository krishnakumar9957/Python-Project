from flask import Flask, render_template
import requests
from post import Post


data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
data_list =[]
for post in data:
     post_data = Post(post["id"], post["title"], post["subtitle"], post["body"])
     data_list.append(post_data)



app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=data_list)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
