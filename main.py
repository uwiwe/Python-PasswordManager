from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Is it ok to save?", message=f"{website_input.get()} \nEmail/Username:"
                                                                          f" {email_input.get()}\nPassword:"
                                                                          f" {password_input.get()}\n\n")
        if is_ok:
            with open("passwords.txt", "a") as passwords:
                passwords.write(f"{website_input.get()} \nEmail/Username: {email_input.get()}\nPassword: "
                                f"{password_input.get()}\n\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@gmail.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
