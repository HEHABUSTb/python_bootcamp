from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
loop = 0
how_many_checks = ''
DEBUG = 1 # change to 60 for the prod

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global loop, how_many_checks

    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text='00:00')
    timer_text.config(text='Timer', fg=GREEN)
    loop = 0
    check_mark.config(text='')
    how_many_checks = ''

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global loop
    loop += 1

    if loop % 8 == 0:
        timer_text.config(text='Long Break', fg=RED)
        count_down(LONG_BREAK_MIN * DEBUG)
    elif loop % 2 == 0:
        timer_text.config(text='Short break', fg=PINK)
        count_down(SHORT_BREAK_MIN * DEBUG)
    else:
        timer_text.config(text='Work Time', fg=GREEN)
        count_down(WORK_MIN * DEBUG)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global how_many_checks, timer

    count_min = int(count / 60)
    count_sec = count % 60
    time = '{:02d}:{:02d}'.format(count_min, count_sec)

    canvas.itemconfig(timer_canvas, text=time)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if loop % 2 == 0:
            how_many_checks += '✔'
            check_mark.config(text=how_many_checks)


# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title('Pomodoro timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Create Canvas image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_canvas = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# "Timer" text on top of the image
timer_text = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_text.grid(column=1, row=0)

# Create buttons
button_start = Button(text='start', command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='reset', command=reset)
button_reset.grid(column=2, row=2)

# Create check mark text = '✔'
check_mark = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
check_mark.grid(column=1, row=3)


window.mainloop()
