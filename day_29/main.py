import random
import json
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
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) > 0 and len(password) > 0:

        try:
            with open("data.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:    
                #Save data
                json.dump(new_data, data_file, indent=4)
        else:
            #Update data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:    
                #Save data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()

    else:
        messagebox.showwarning(title="Oooops", message="Please don't leave any fields empty")        


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = entry_website.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showwarning(title="Oooops", message="There is no such website in database")    
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"email: {data[website]["email"]}\npassword: {data[website]["password"]}")
        else:
            messagebox.showwarning(title="Oooops", message="There is no such website in database")


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

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_username = Entry(width=38)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "mail@gmail.com")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_search = Button(text="Search", width=13, command=find_password)
button_search.grid(column=2, row=1)
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()