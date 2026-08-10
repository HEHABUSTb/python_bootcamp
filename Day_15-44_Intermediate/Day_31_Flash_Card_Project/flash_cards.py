from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA WORK------------------------------- #
# Read csv and create data frame
data = pandas.read_csv("data/words_to_learn.csv")
data = [{row.Polish: row.Russian} for (index, row) in data.iterrows()]
# print(data)

polish_word = ''
russian_word = ''


# ---------------------------- REMOVE WORD------------------------------- #


def move_word_to_learned():
    global polish_word, russian_word

    # Add word to learned_words.csv
    learned_words = pandas.read_csv("data/learned_words.csv")
    # print(data)
    learned_words.loc[len(learned_words)] = [polish_word, russian_word]
    learned_words.to_csv("data/learned_words.csv", index=False)
    # print(data)

    # Remove word from words_to_learn.csv
    to_learn = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
    # print(to_learn)
    to_learn.remove({'Polish': polish_word, 'Russian': russian_word})
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # print(data)

    next_card()


# ---------------------------- NEXT CARD------------------------------- #
def next_card():
    global polish_word, russian_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data)
    polish_word = list(random_word.keys())[0]
    russian_word = list(random_word.values())[0]

    # print(russian_word, polish_word)
    # print(random_word)

    # Show random word
    canvas.itemconfig(canvas_image, image=image_front)
    canvas.itemconfig(title, text='Русский', fill='black')
    canvas.itemconfig(word, text=russian_word, fill='black')

    # Start timer
    flip_timer = window.after(ms=3000, func=flip_card)


# ---------------------------- FLIP CARD------------------------------ #
def flip_card():
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(title, text='Polski', fill='white')
    canvas.itemconfig(word, text=polish_word, fill='white')


# ---------------------------- UI SETUP ------------------------------- #

# Create window and put logo inside
window = Tk()
window.title('Flash cards app')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Timer announce for looping cancel after many pushes in next card
flip_timer = window.after(ms=3000, func=flip_card)
# window.eval('tk::PlaceWindow . center') that shit doesn't work properly

# Create Canvas image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_front = PhotoImage(file='images/card_front.png')
image_back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=image_front)
canvas.grid(row=0, column=0, columnspan=2)

# Create text
title = canvas.create_text(400, 150, tag="title", text='Русский', font=('Ariel', 40, 'italic'))

word = canvas.create_text(400, 263, tag="word", text='', font=('Ariel', 50, 'bold'))

# buttons
image_right = PhotoImage(file='images/right.png')
button_right = Button(image=image_right, highlightthickness=0, command=move_word_to_learned)
button_right.grid(row=1, column=1)

image_wrong = PhotoImage(file='images/wrong.png')
button_right = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=0)

# Show words
next_card()
window.mainloop()
