from tkinter import *

window = Tk()
window.title("Widgets examples")
window.minsize(width=500, height=500)

# TODO Creating a label
my_label = Label(text="I'm a label", font=("Arial", 24, "normal"))
my_label.pack()
# my_label.pack(side="left")

def button_clicked():
    print("Did you just click me?!")
    # TODO Get text from the text entry
    entry_text = text_entry.get()
    # TODO Display text from the text entry on the label
    my_label.config(text=entry_text)


# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# TODO Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# TODO Text entry
text_entry = Entry(width= 10)
text_entry.pack()




window.mainloop()
