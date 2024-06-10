from tkinter import *


def button_click():
    my_label["text"] = my_input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label["text"] = "Button clicked"
#my_label.config(text="Another new text")
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="Click me", command=button_click)
new_button.grid(column=2, row=0)


#Entry
my_input = Entry(width=10)
print(my_input.get())
my_input.grid(column=3, row=2)


window.mainloop()