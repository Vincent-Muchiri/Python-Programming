from tkinter import *

FONT_DETAILS = ("Arial", 12, "normal")

# TODO Create window
window = Tk()
window.title("User Registration")
window.minsize(width=500, height=800)
window.config(padx=20, pady=20)

# TODO Create a phantom grid
phantom_label = Label()
phantom_label.grid(row=0, column=0)

# TODO Create a label "Please enter your details"
prompt_label = Label(text="Please enter your details", font=("Arial", 14, "normal"))
prompt_label.config()
# prompt_label.grid(row=0, column=2)
prompt_label.place(x=110, y=0)

# TODO Create a label and an entry for your first and second name
first_name_label = Label(text="First name", font=FONT_DETAILS)
first_name_label.config(pady=20, padx=10)
first_name_label.grid(row=3, column=0)

first_name_entry = Entry()
first_name_entry.config(width=20)
first_name_entry.grid(row=3, column=1)

last_name_label = Label(text="Last name", font=FONT_DETAILS)
last_name_label.config(pady=20, padx=10)
last_name_label.grid(row=4, column=0)

last_name_entry = Entry()
last_name_entry.config(width=20)
last_name_entry.grid(row=4, column=1)

# TODO Create radio buttons for gender
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
male_button = Radiobutton(text="", value=1, variable=radio_state, command=radio_used)
female_button = Radiobutton(text="", value=2, variable=radio_state, command=radio_used)
other_button = Radiobutton(text="", value=3, variable=radio_state, command=radio_used)

male_label = Label(text="Male", font=FONT_DETAILS)
male_label.config()
male_label.grid(row=6, column=0)

female_label = Label(text="Female", font=FONT_DETAILS)
female_label.config()
female_label.grid(row=7, column=0)

other_label = Label(text="Other", font=FONT_DETAILS)
other_label.config()
other_label.grid(row=8, column=0)

male_button.grid(row=6, column=1)
female_button.grid(row=7, column=1)
other_button.grid(row=8, column=1)


# TODO Create a spinbox for selecting the date of birth
other_label = Label(text="Age", font=FONT_DETAILS)
other_label.config(pady=25)
other_label.grid(row=9, column=0)

def spinbox_used():
    #gets the current value in spinbox.
    print(age_spinbox.get())
age_spinbox = Spinbox(from_=18, to=100, width=3, command=spinbox_used)
age_spinbox.grid(row=9, column=1)


# TODO Create a scale for selecting the current savings
other_label = Label(text="What's your current salary?", font=FONT_DETAILS)
other_label.config(pady=25)
other_label.grid(row=10, column=1)

#Called with current scale value.
def scale_used(value):
    print(value)
savings = Scale(from_=0, to=200000 , command=scale_used)
savings.grid(row=11, column=1)

# TODO Create a text box asking the user why they want the scholarship
justification = Text(height=5, width=30)
justification.config()
#Puts cursor in textbox.
justification.focus()
#Adds some text to begin with.
justification.insert(END, "Justify why you want a scholarship")
#Get's current value in textbox at line 1, character 0
print(justification.get("1.0", END))
justification.grid(row=12, column=1)

# TODO Listbox of showing the user all his/her details
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
listbox.config()
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=13, column=1)


# TODO Create button to save the data into a CSV
save_button = Button(text="Save Details")
save_button.config(width=30)
save_button.grid(row=14, column=1)



window.mainloop()
