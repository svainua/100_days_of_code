from tkinter import *

def calculate():
    miles = float(my_input.get())
    label_2["text"] = int(miles * 1.609)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


label_1 = Label(text="is equal to", font=("Arial", 24, "bold"))
label_1.grid(column=0, row=1)

label_2 = Label(text="0", font=("Arial", 24, "bold"))
label_2.grid(column=1, row=1)

label_3 = Label(text="Miles", font=("Arial", 24, "bold"))
label_3.grid(column=2, row=0)

label_4 = Label(text="Km", font=("Arial", 24, "bold"))
label_4.grid(column=2, row=1)

my_input = Entry(width=10)
my_input.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()