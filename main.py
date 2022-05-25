BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *


window = Tk()
#my_image = PhotoImage(image=card_back.png)
window.title("Flash_card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)


canvas= Canvas(width=800, height=600)
card_front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 265, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
canvas.pack()






window.mainloop()

