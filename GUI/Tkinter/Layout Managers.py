from tkinter import *

# TODO Create window
window = Tk()
window.title("Tkinter Layout Managers")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)


# TODO Pack()
# Starts placing widgets one below another
# pack() and grid() can not be used together
my_label = Label(text="Default Pack Label", font=("Ariel", 12, "normal"))
# my_label.pack()

my_button = Button(text="Pack Left Button")
# my_button.pack(side="left")

my_button2 = Button(text="Pack Right Button")
# my_button2.pack(side="right")

# TODO Place
# Allows precise positioning
place_label = Label(text="Place label")
place_label.place(x=300, y=300)

# TODO Grid
# Relative to other widgets i.e. there has to be a widget in row = 0 and column = 0
# pack() and grid() cannot be used together
grid_label = Label(text="Grid Label", padx=10, pady=20)
grid_label.grid(column= 0, row=0)

grid_button = Button(text="Grid Button", padx= 20)
grid_button.grid(row=0, column=1)





window.mainloop()