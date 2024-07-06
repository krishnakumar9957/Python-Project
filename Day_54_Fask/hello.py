from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style = 'text-align:center' >hello world!</h1>" \
           "<p>thi sis praagraph.</p>" \
           "<img src= 'https://media0.giphy.com/media/rrTXn4zEMp008/200.webp?cid=790b7611owgcshcohksmscapq6omd2us3yavtfqu8z3gdeeq&ep=v1_gifs_search&rid=200.webp&ct=g',width=500>"


@app.route("/bye")
def bye():
    return "bye"


@app.route("/username/<name>")
def greet(name):
    return (f'Hello {name}!')


if __name__ == "__main__":
    app.run(debug=True)
