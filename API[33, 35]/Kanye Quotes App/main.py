# ---------------------------------------------- IMPORTS ----------------------------------------------------------
import requests
from tkinter import *

# ----------------------------------------------- CONSTANTS & VARIABLES -----------------------------------------------
QUOTES_FONT = ("Calibri", 16, "normal")


# ------------------------------------------------ FUNCTIONS ---------------------------------------------------------
def next_quote():
    # TODO Get data from the API
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quotes_dict = response.json()
    quote = quotes_dict["quote"]

    # TODO Refresh the text on the canvas
    canvas.itemconfig(canvas_text, text=quote)
    pass


# ----------------------------------------------- GUI -----------------------------------------------------------------
# TODO Setup the window
window = Tk()
window.config(padx=50, pady=20)
window.minsize(width=400, height=600)
window.geometry("410x600")
window.title("Kanye Quotes App")


# TODO Register images
quotes_icon = PhotoImage(file="images/3057671_media_quote_social_icon.png")
quotes_bg = PhotoImage(file="images/background.png")
btn_bg = PhotoImage(file="images/kanye.png")

# TODO Add app icon
window.iconphoto(False, quotes_icon)

# TODO Create canvas
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 200, image=quotes_bg)
canvas.grid(row=0, column=0, columnspan=3)

# TODO Create text
canvas_text = canvas.create_text(140, 190, width=210, text="Kanye Quotes Will \nBe Displayed Here",
                                 font=QUOTES_FONT, justify="center")

# TODO Create button
btn = Button(command=next_quote)
btn.config(image=btn_bg, relief="flat")
btn.grid(row=1, column=1)

window.mainloop()
