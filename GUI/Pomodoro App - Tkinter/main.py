
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECKMARK_X = 105

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # count_down(minutes * 60)
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", font=(FONT_NAME, 24, "bold"), fg= RED)
    elif reps % 2 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", font=(FONT_NAME, 24, "bold"), fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", font=(FONT_NAME, 24, "bold"), fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    import math
    global CHECKMARK_X
    count_min = math.floor(seconds/60)
    count_sec = seconds % 60
    if seconds < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    if seconds >= 0:
        # print(count)
        tomato.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        window.after(1000, count_down, seconds-1)
    else:
        start_timer()
        if reps % 2 ==0:
            CHECKMARK_X += 20
            check_mark_label.place(x=CHECKMARK_X, y=310)


# ---------------------------- UI SETUP ------------------------------- #
# TODO Create a window
from tkinter import *
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# TODO Create a label "Timer"
timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"))
timer_label.config(bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# TODO Create a canvas
tomato = Canvas(width=207, height=224)
tomato_pic = PhotoImage(file="tomato.png")
tomato.create_image(103, 112, image=tomato_pic)
timer_text = tomato.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
tomato.config(bg=YELLOW, highlightthickness=0)
tomato.grid(row=1, column=1)

# TODO Create the start button
start_button = Button(text="Start", command=start_timer)
start_button.config(bg=YELLOW, highlightthickness=0)
start_button.grid(row=2, column=0)

# TODO Create the reset button
reset_button = Button(text="Reset")
reset_button.config(bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2)

# TODO Create a check mark label
check_mark_label = Label(text="✅")
check_mark_label.config(fg=GREEN, bg=YELLOW)
check_mark_label.place(x=CHECKMARK_X, y=310)

window.mainloop()
