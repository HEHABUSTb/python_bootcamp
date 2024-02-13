from tkinter import *
from tkinter import messagebox
import csv

FONT = ('Courier', 12, 'normal')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(mode='a'):
    # Set mode='w' if you want to rewrite file
    # Get data from entry fields
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    header = ['website', 'username', 'password']
    data = [website, username, password]

    if '' in data:
        messagebox.showerror(title='Some Fields are empty', message="Please don't leave any fields empty!")
        return None

    # Check data is correct in message box
    answer = messagebox.askokcancel(title=website, message=f"These data you provide is correct?\nUsername:{username}\nPassword:{password}")
    if answer is False:
        pass
    else:
        # Save data in 'secret.csv'
        with open('secret.csv', mode, newline='') as file:
            writer = csv.writer(file)
            if mode == 'w':
                writer.writerow(header)
            writer.writerow(data)

        # Clearing entry fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, 'test@test.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
password_button = Button(text='Generate Password')
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
