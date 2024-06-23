import random
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for i in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) > 0 and len(password) > 0:
        is_ok =messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password}\n Is it OK to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()
    else:
        messagebox.showwarning(title="Oooops", message="Please don't leave any fields empty")        


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = Entry(width=38)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_username = Entry(width=38)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "sva.in.ua@gmail.com")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()