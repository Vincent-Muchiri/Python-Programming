# ----------------------------------------------------- IMPORTS --------------------------------------------------------
from tkinter import *
from tkinter import Tk
from data import trivia_ques_list
# ----------------------------------------------- CONSTANTS & VARIABLES ------------------------------------------------
FONT = ("Calibre", 18, "normal")
question_index = 0
points = 0


# ----------------------------------------------------- FUNCTIONS ------------------------------------------------------
def right_btn_clicked():
    global question_index, points

    question_index += 1
    if question_index <= 9:
        question = trivia_ques_list[question_index]['question']
        canvas.itemconfig(question_canvas, text=question)

        answer = trivia_ques_list[question_index]['answer'].lower()

        if answer == "true":
            points += 1
    else:
        canvas.itemconfig(question_canvas, text=f"You've scored {points} points")


def wrong_btn_clicked():
    global question_index, points

    question_index += 1
    if question_index <= 9:
        question = trivia_ques_list[question_index]['question']
        canvas.itemconfig(question_canvas, text=question)

        answer = trivia_ques_list[question_index]['answer'].lower()

        if answer == "false":
            points += 1
    else:
        canvas.itemconfig(question_canvas, text=f"You've scored {points} points")


# -------------------------------------------------------- GUI ---------------------------------------------------------
window = Tk()
window.title("Trivia Game")
window.minsize(width=400, height=500)
window.config(padx=20, pady=20)

# TODO Add window icon
app_icon = PhotoImage(file="./images/brain.png")
window.iconphoto(False, app_icon)
window.config(bg="white")

# TODO Create canvas
canvas = Canvas(width=350, height=350)
canvas.config(bg="white", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# TODO Create text in the canvas
question_canvas = canvas.create_text(175, 175, width=300, text=trivia_ques_list[question_index]['question'], font=FONT,
                                     justify="center")

# TODO Create buttons
right_btn = Button(command=right_btn_clicked)
right_img = PhotoImage(file="./images/correct_128.png")
right_btn.config(width=128, height=128, image=right_img, relief="flat", bg="white")
right_btn.grid(row=1, column=0)

wrong_btn = Button(command=wrong_btn_clicked)
wrong_img = PhotoImage(file="./images/x-button_128.png")
wrong_btn.config(width=128, height=128, image=wrong_img, relief="flat", bg="white")
wrong_btn.grid(row=1, column=1)

window.mainloop()
