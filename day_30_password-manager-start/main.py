from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_input.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username = Label(text="Email/Username: ")
username.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

add_button = Button(text="Add", width=51, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(column=2, row=3)

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

email_input = Entry(width=60)
email_input.grid(column=1, row=2, columnspan=2)

website_input = Entry(width=60)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

window.mainloop()
