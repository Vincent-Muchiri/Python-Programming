#----------------------------------------------------LIBRARIES----------------------------------------------------------
from tkinter import *
import tkinter.ttk as ttk
import pandas
import random


#-----------------------------------------------CONSTANTS & VARIABLES---------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_eng_word = ""

#----------------------------------------------------FUNCTIONS----------------------------------------------------------
# TODO Open the CSV file with the Zulu words
zulu_words_df = pandas.read_csv("data/1000 Frequent Zulu Words.csv")
zulu_words_list = zulu_words_df["Zulu words"].to_list()
english_words_list = zulu_words_df["in English"].to_list()

def new_card():
    global current_eng_word
    # TODO Change the word to Zulu
    current_zulu_word = random.choice(zulu_words_list)
    current_word_index = zulu_words_list.index(current_zulu_word)
    current_eng_word = english_words_list[current_word_index]

    # TODO Change word
    canvas.itemconfig(current_card, image=zulu_card)
    canvas.itemconfig(language, text="Zulu", fill = "black")
    canvas.itemconfig(word, text=current_zulu_word, fill = "black")

    window.after(5000, flip_card)



def flip_card():
    canvas.itemconfig(current_card, image=english_card)
    canvas.itemconfig(language, text="English", fill = "white")
    canvas.itemconfig(word, text=current_eng_word, fill="white")




#-------------------------------------------------------GUI-------------------------------------------------------------
# TODO Create window
window = Tk()
window.title("Flashy: Zulu")
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(6000, func=new_card)

zulu_card = PhotoImage(file="images/card_front.png")
english_card = PhotoImage(file="images/card_back.png")

# TODO Create canvas
canvas = Canvas(width=800, height=526)
current_card = canvas.create_image(400, 263, image=zulu_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# TODO Place texts on the canvas
language = canvas.create_text(400, 150, font=LANGUAGE_FONT, text="Zulu")
word = canvas.create_text(400, 250, font=WORD_FONT, text="Word")

# TODO Create wrong button
wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(command=new_card)
wrong_btn.config(image=wrong_btn_image, bg=BACKGROUND_COLOR, relief="flat")
wrong_btn.grid(row=1, column=0)

# TODO Create right button
right_btn_image = PhotoImage(file="images/right.png")
right_btn = Button(command=new_card)
right_btn.config(image=right_btn_image, bg=BACKGROUND_COLOR, relief="flat")
right_btn.grid(row=1, column=1)

new_card()

window.mainloop()
