from tkinter import *
import pandas
import Log_window
import tkinter.ttk as ttk
from tkinter import messagebox

# history_window = Log_window.log_window

# TODO Create a function to get miles, convert miles to km and display the km to a label after pressing the button
conversion_dict = {}
miles_list = []
km_list = []

# TODO Create a text file to save the conversion history
with open("conversion_history.txt", mode="a") as conversion_file:
    conversion_file.write("miles | km\n")

def convert():
    miles = float(miles_entry.get())
    km = miles * 1.609
    converted_km_label.config(text=f"{round(km)}")

    # TODO Add the miles and km values to list with the last entry being index 0
    miles_list.insert(0, miles)
    km_list.insert(0, km)
    # TODO Add the conversion to a dictionary using a list
    conversion_dict["Miles"] = miles_list
    conversion_dict["Km"] = km_list
    # print(conversion_dict)

    # TODO Save the conversion to a csv file
    conversion_dataframe = pandas.DataFrame(conversion_dict)
    conversion_dataframe.to_csv("conversion_history.csv")

    #TODO Save the conversion to a text file
    with open("conversion_history.txt", mode="a") as conversion_file:
        conversion_file.write(f"{miles} | {km}\n")

    # TODO Return cursor to miles entry
    miles_entry.focus()

# TODO Create function to clear history
def clear_history():
    print("")
    conversion_dict = {}
    # TODO Save the conversion to a csv file
    conversion_dataframe = pandas.DataFrame(conversion_dict)
    conversion_dataframe.to_csv("conversion_history.csv")
    # print("History Cleared!")
    messagebox.showinfo(title="Clear history", message="History has been cleared!")

    # TODO Clear the text file
    with open("conversion_history.txt", "w") as  conversion_file:
        conversion_file.write("")

# TODO Create program to open new window
def history_window():
    # TODO Create program window
    # from tkinter import *
    # new_window = Tk()
    # new_window.title("Conversion History")
    # new_window.minsize(width=250, height=400)
    # new_window.config(padx=10, pady=10)

    conversion_data = pandas.read_csv("conversion_history.csv")
    print(conversion_data)
    new_label = Label(text="New Label")

    # for i in range(5):
    #     conversion_data_label = Label(text=i)
    #     conversion_data_label.config()
    #     conversion_data_label.grid(row=i, column=0)

    # new_window.mainloop()

# TODO Create a window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# TODO Set window styling
style = ttk.Style(window)
window.tk.call('source', '../_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Create a label "is equal to"
equal_to_label = Label(text="is equal to:")
equal_to_label.config(padx=10)
equal_to_label.grid(row=1, column=0)


# TODO Create an entry for miles
miles_entry = ttk.Entry()
miles_entry.config(width=13)
# miles = miles_entry.get()
miles_entry.focus()
miles_entry.insert(END, 0)
miles_entry.grid(row=0, column=1)

# TODO Crete a label for "Miles" and "Km"
miles_label = Label(text="Miles")
miles_label.config(padx=50)
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.config(padx=10)
km_label.grid(row=1, column=2)

# TODO Create a label for converted km
converted_km_label = Label(text="0")
converted_km_label.config(padx=50, pady=20)
converted_km_label.grid(row=1, column=1)

# TODO Create a button "Convert"
convert_button = ttk.Button(window, style="Accentbutton", text="Convert", command=convert)
convert_button.config(width=10)
convert_button.grid(row=2, column=0)

# TODO Create a button to clear the log file
clear_button = ttk.Button(window, style="Accentbutton",text="Clear History", command=clear_history)
clear_button.config()
clear_button.grid(row=2, column=1)

# TODO Create a button to open the log file
history_button =ttk.Button(window, style="Accentbutton",text="Conversion History", command=history_window)
history_button.config()
history_button.grid(row=2, column=2)

window.mainloop()
