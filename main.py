BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

data= pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    current_card["French"]


window = Tk()
window.title("Flash_card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)


canvas= Canvas(width=800, height=600)
card_front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 265, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "bold"))
canvas.create_text(400, 250, text="word", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=cross_image, highlightthickness=0, command= next_card)
unkown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command= next_card)
known_button.grid(row=1, column=1)





window.mainloop()

