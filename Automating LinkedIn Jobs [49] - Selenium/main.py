from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from pprint import pprint

# TODO Import classes
from submit_query import SubmitQuery


def apply():
    # TODO Get all the values from the entries and text
    email = email_entry.get()
    password = password_entry.get()
    query = search_text.get("1.0", END)

    # TODO Create object
    submit_query = SubmitQuery(email=email, password=password, query_str=query)

    # TODO Search and apply
    submit_query.search()


# TODO Create a window
window = Tk()
window.title("Automated LinkedIn Job Application")
window.geometry("370x330+200+200")
# window.minsize(width=400, height=400)
window.config(padx=10, pady=10)

# TODO Link the styling file
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Create a 'login details' label frame
login_frame = ttk.Labelframe(text="Login Details")
login_frame.pack(fill="both")
login_frame.config(padding=10)

# TODO Add the email and password labels and entry boxes
email_label = ttk.Label(login_frame, text="Email address:")
email_label.grid(column=0, row=0)

email_entry = ttk.Entry(login_frame)
email_entry.config(width=30)
email_entry.focus()
email_entry.insert(0, "vincentmuchiri1@gmail.com")
email_entry.grid(column=1, row=0)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(column=0, row=1)

password_entry = ttk.Entry(login_frame)
password_entry.config(width=30)
password_entry.insert(0, "Virt84788676!")
password_entry.grid(column=1, row=1, padx=20, pady=10)

# TODO Create a 'Search query' label frame
search_frame = ttk.Labelframe(text="Search query")
search_frame.pack(fill="both", pady=20)
search_frame.config(padding=10)

# TODO Create a multi line text box
search_text = Text(search_frame, height=3)
# Adds some text to begin with.
# search_text.insert(END, "Enter search parameters seperated by a ,")
search_text.insert(END, "graduate trainee, consultant")
# print(search_text.get("1.0", END))
search_text.pack()

# TODO Create an apply button
apply_btn = ttk.Button(text="Apply", style="Accentbutton", command=apply)
apply_btn.pack()


window.mainloop()
