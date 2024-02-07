from tkinter import *


def convert_miles():
    miles = entry.get()
    if miles != '':
        km = float(miles) * 1.60934
        # print(km)
        label_kilometers.config(text=f"{km:.2f}")
    else:
        pass

# Window creating
window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

# Label description
label_equal = Label(text='is equal to ')
label_equal.grid(column=0, row=1)

# Label "Miles"
label_miles = Label(text='Miles')
label_miles.grid(column=2, row=0)

# User entry input field
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label with calculated kilometers
label_kilometers = Label(text='0')
label_kilometers.grid(column=1, row=1)

# Label text with kilometers
label_text_kilometers = Label(text='kilometers')
label_text_kilometers.grid(column=2, row=1)

# Button to calculate miles to kilometers
button = Button(text='Calculate', command=convert_miles)
button.grid(column=1, row=2)

window.mainloop()
