from tkinter import *
import pandas

FONT = ("Arial", 16, "normal")

# TODO Create program window

def log_window():
    new_window = Tk()
    new_window.title("Conversion History")
    new_window.minsize(width=250, height=400)
    new_window.config(padx=10, pady=10)

    miles_title = Label(text="Miles", font=FONT)
    miles_title.config(padx=20)
    miles_title.grid(row=0, column=1)

    km_title = Label(text="Km", font=FONT)
    km_title.config(pady=20)
    km_title.grid(row=0, column=2)

    conversion_data = pandas.read_csv("conversion_history.csv")
    # print(conversion_data.Miles)
    # print(len(conversion_data.Miles))
    # print(conversion_data.Miles[1])

    for index in range(len(conversion_data.Miles)):
        index_label = Label(text=index, font=FONT)
        # index_label.config(padx=20, pady=10)
        index_label.grid(row=index+1, column=0)

        miles_label = Label(text=conversion_data.Miles[index], font=FONT)
        miles_label.grid(row=index+1, column=1)

        km_label = Label(text=conversion_data.Km[index], font=FONT)
        # km_label.config(padx=20)
        km_label.grid(row=index+1, column=2)

    new_window.mainloop()
