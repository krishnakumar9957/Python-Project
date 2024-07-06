from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route('/')
def main():
    return "<h1>Guess the number 0 to 9.</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:guess>')
def guess_number(guess):
    if guess <random_number:
        return "<h1 style='color: red'> It is too low, Try again!.</h1>" \
               "<img src ='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width = 300 >"

    elif guess > random_number:
        return "<h1 style = 'color: purple'>It is too High, Try again!.</h1>" \
               "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width= 300 >"

    else:
        return "<h1 style = 'color: green'> You found me.</h1>" \
               "<img src= 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width = 300> "





if __name__ == "__main__":
    app.run(debug=True)