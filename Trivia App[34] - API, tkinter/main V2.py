# ----------------------------------------------------- IMPORTS --------------------------------------------------------
from tkinter import *
from tkinter import Tk, messagebox
from data import trivia_ques_list
import data as dt

# ----------------------------------------------- CONSTANTS & VARIABLES ------------------------------------------------
FONT = ("Calibre", 18, "normal")

question_index = 0
score = 0


# ----------------------------------------------------- FUNCTIONS ------------------------------------------------------
def get_next_question():
    global question_index

    # TODO Check if all the questions have been displayed
    if question_index <= 2:
        # TODO Get next question
        question = trivia_ques_list[question_index]['question']

        # TODO Add the question to the canvas
        canvas.itemconfig(text_canvas, text=question)

        # TODO Change the canvas background
        canvas.config(bg="white")
    else:
        # TODO Change the canvas background
        canvas.config(bg="white")



        the_end()


def the_end():
    global question_index

    # TODO Show score on the canvas
    canvas.itemconfig(text_canvas, text=f"You've scored {score} points")
    
    # TODO Make sure the buttons can't be pressed
    wrong_btn.config(state="disabled")
    right_btn.config(state="disabled")

    # TODO Prompt whether to restart or end
    response = messagebox.askyesno(title="Game Over", message=f"You,ve scored {score} points.\n"
                                                              f"Do you want to continue with the game?")
    if response:
        from data import trivia_json_data
        question_index = 0
        get_next_question()
    elif response:
        window.quit()


def check_answer(response):
    global score, question_index

    # TODO Check if there's any answers left
    if question_index <= 9:
        # TODO Get answer
        answer = trivia_ques_list[question_index]['answer']

        # TODO If answer is correct
        if response == answer:
            # TODO Increase the score
            score += 1

            # TODO Update the score label
            score_label.config(text=f"Score: {score}")

            # TODO Notify the user
            canvas.config(bg="green")
        else:
            # TODO Notify the user
            canvas.config(bg="red")

        # TODO Increase the question index
        question_index += 1


def right_btn_clicked():
    response = "True"

    # TODO Check answer
    check_answer(response)

    # TODO Go to next answer
    window.after(1000, get_next_question)


def wrong_btn_clicked():
    response = "False"

    # TODO Check answer
    check_answer(response)

    # TODO Go to next answer
    window.after(1000, get_next_question)
    print(score)


# -------------------------------------------------------- GUI ---------------------------------------------------------
window = Tk()
window.title("Trivia Game")
window.minsize(width=400, height=500)
window.config(padx=20, pady=20)

# TODO Add window icon
app_icon = PhotoImage(file="./images/brain.png")
window.iconphoto(False, app_icon)
window.config(bg="white")

# TODO Create the score label
score_label = Label(text=f"Score: 0", font=("Calibre", 12, "normal"))
score_label.config(bg="white")
score_label.grid(row=0, column=1)

# TODO Create canvas
canvas = Canvas(width=350, height=350)
canvas.config(bg="white", highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)

# TODO Create text in the canvas
text_canvas = canvas.create_text(175, 175, width=300, text=trivia_ques_list[question_index]['question'], font=FONT,
                                 justify="center")

# TODO Create buttons
right_btn = Button(command=right_btn_clicked)
right_img = PhotoImage(file="./images/correct_128.png")
right_btn.config(width=128, height=128, image=right_img, relief="flat", bg="white")
right_btn.grid(row=2, column=0)

wrong_btn = Button(command=wrong_btn_clicked)
wrong_img = PhotoImage(file="./images/x-button_128.png")
wrong_btn.config(width=128, height=128, image=wrong_img, relief="flat", bg="white")
wrong_btn.grid(row=2, column=1)

window.mainloop()
