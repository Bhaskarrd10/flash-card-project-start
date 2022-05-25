BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

data= pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

window = Tk()
window.title("Flash_card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer =window.after(3000, func=flip_card)

canvas= Canvas(width=800, height=600)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 265, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "bold"))
card_word = canvas.create_text(400, 250, text="word", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=cross_image, highlightthickness=0, command= next_card)
unkown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command= next_card)
known_button.grid(row=1, column=1)

next_card()



window.mainloop()

