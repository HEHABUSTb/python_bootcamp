from tkinter import *

FONT = ('Courier', 12, 'normal')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


# Create window and put logo inside
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

# Create Canvas image and timer
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text='Website:', font=FONT)
website_text.grid(row=1, column=0, sticky="EW")
username_text = Label(text='Email/Username:', font=FONT)
username_text.grid(row=2, column=0, sticky="EW")
password_text = Label(text='Password:', font=FONT)
password_text.grid(row=3, column=0, sticky="EW")

# Fields Entry
website_field = Entry(width=35)
website_field.grid(row=1, column=1, columnspan=2, sticky="EW")
username_field = Entry(width=35)
username_field.grid(row=2, column=1, columnspan=2, sticky="EW")
password_field = Entry(width=21)
password_field.grid(row=3, column=1, sticky="EW")

# Buttons
password_button = Button(text='Generate Password')
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text='Add', width=35)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()