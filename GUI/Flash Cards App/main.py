# ----------------------------------------------LIBRARIES, CLASSES & METHODS--------------------------------------------
from tkinter import *
import pandas
import random

# ----------------------------------------------CONSTANTS & VARIABLES---------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

random_word = "Word"

current_card = {}


# --------------------------------------------------FUNCTIONALITY-------------------------------------------------------
# TODO Import csv data of words to learn
try:
    words_to_learn_df = pandas.read_csv("data/Words To Learn.csv")

except FileNotFoundError:
    # print("File not found")

    words_to_learn_df = pandas.read_csv("data/1000 Frequent Zulu Words.csv")

    # TODO If the file doesn't exist create it
    words_to_learn_df.to_csv("./data/Words To Learn.csv")
    # print("File created")

finally:
    # TODO Convert the data to a list of dictionary
    words_to_learn_list = words_to_learn_df.to_dict(orient="records")


# TODO Show next card
def next_card():
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(words_to_learn_list)
    cards.itemconfig(card_bg, image=front_card)
    cards.itemconfig(card_title, text="Zulu", fill="black")
    cards.itemconfig(card_word, text=current_card["Zulu words"], fill="black")

    flip_timer = window.after(3000, func=flip_card)


# TODO Show the translation of the word in English
def flip_card():
    cards.itemconfig(card_title, text="English", fill="white")
    cards.itemconfig(card_word, text=current_card["in English"], fill="white")
    cards.itemconfig(card_bg, image=back_card)


# TODO Remove the words that the user already knows from the list of words displayed
def is_known():
    global current_card

    # TODO Remove the known word from the list of words to learn
    try:
        words_to_learn_list.remove(current_card)
    except ValueError:
        pass
    else:
        # TODO Rewrite the data in the 'Words To Learn.csv' file with the new list
        new_words_to_learn_df = pandas.DataFrame(words_to_learn_list)
        new_words_to_learn_df.to_csv("./data/Words To Learn.csv")

    flip_card()


# -------------------------------------------------------UI-------------------------------------------------------------
# TODO Create a window
window = Tk()
window.title("Flashy: Zulu")
window.minsize(width=890, height=730)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# TODO Flip the card after 3s
flip_timer = window.after(3000, func=flip_card)


# TODO Create a card canvas
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
current_bg_card = front_card

cards = Canvas(width=800, height=526)
cards.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = cards.create_image(400, 263, image=current_bg_card)
cards.grid(row=0, column=0, columnspan=2)

card_title = cards.create_text(400, 150, text="", font=LANGUAGE_FONT)
card_word = cards.create_text(400, 263, text="8", font=WORD_FONT)

# TODO Create the "wrong" button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=next_card)
wrong_button.config(image=wrong_image, bg=BACKGROUND_COLOR, relief="flat")
wrong_button.grid(row=1, column=0)

# TODO Create the "right" button
right_button = Button(command=is_known)
right_image = PhotoImage(file="images/right.png")
right_button.config(image=right_image, relief="flat", bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

# TODO Rewrite the default values of the 'word'
next_card()

window.mainloop()
